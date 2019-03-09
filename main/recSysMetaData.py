import pandas as pd
from ast import literal_eval
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class recSysMetaData:
	def __init__(self):
		self.location_clean = "../data/merged_clean.csv"
		self.model_location = "../model_output/metadata_model_output.txt"
		self.df = pd.read_csv(self.location_clean)
		self.count = CountVectorizer(stop_words='english')

	def build_model(self):
		df = self.df
		def create_soup(df):
			soup = ''.join(df['keywords']) + " " \
				+ ''.join(df['genres'])+ " " \
				+ ''.join(df['cast']) + " " \
				# + ''.join(df['director'])
			return soup

		df['soup'] = df.apply(create_soup, axis=1)
		count_matrix = self.count.fit_transform(df['soup'])
		#compute cosine similarity 
		cosine_sim = cosine_similarity(count_matrix, count_matrix)
		df = df.reset_index()
		indices = pd.Series(df.index, index=df['title'])
		return cosine_sim


	def recommend(self, title):
		cosine_sim = self.build_model()
		print("INFO: loaded the model")
		#making the title an index and the index a feature 
		indices = pd.Series(self.df.index ,index=self.df['title']).drop_duplicates()
		#obtain the index of the movie that matches the title argument 
		idx = indices[title]

		"""
		1) get the pairwise similarty scores of all movies with index based on 
		title lookup 
		2) Convert result into a list of tuples where the first element 
		is the position  and the second is the similarity score
		3)  
		
		"""
		sim_scores = list(enumerate(cosine_sim[idx]))
		"""
		sort the tuple based on similarity scores in descending order based on second
		element x[1] which in this case is the similarit score
		"""
		sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
		#get the top 10 most similar movies, ignoring the first which is always the title selected
		sim_scores = sim_scores[1:11]
		# get the movie indices from these scores to march against the dataframe
		# where indices are titles and titles are indices, filter by indices
		movie_indices = [i[0] for i in sim_scores]
		#finally return the tile selected
		return self.df['title'].iloc[movie_indices]


def main(title):
	recommendations = recSysMetaData().recommend(title='The Lion King')
	print(recommendations)
	return 


print(recSysMetaData().recommend(title='The Lion King'))