import pandas as pd 
import numpy as np 
#Import TfIdfVectorizer from scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import sys
import os

class recSysContent:
	def __init__(self):
		self.location_clean = "../data/merged_clean.csv"
		self.model_location = "../model_output/content_model_output.txt"
		self.df = pd.read_csv(self.location_clean)


	def build_model(self,save=False):
		#transform data into tdidf matrix
		tfidf = TfidfVectorizer(stop_words='english')
		self.df['overview'] = self.df['overview'].fillna('')
		tfidf_matrix = tfidf.fit_transform(self.df['overview'])
		#calculate the similarity distance
		cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
		
		if save == True:
			print("INFO: saving model to {0}".format(self.model_location))
			np.savetxt(self.model_location, cosine_sim)
		else:
			print("INFO: model saved in memory and not locally")
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
	recommendations = recSysContent().recommend(title=title)
	print(recommendations)
	return None


if __name__ == '__main__':
	title = "Toy Story"
	main(title)

