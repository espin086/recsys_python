import pandas as pd 
import numpy as np 
#Import TfIdfVectorizer from scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import sys
import os

class recSysContent:
	def __init__(self):
		self.location_clean = "../data/movies_metadata_clean.csv"
		self.model_location = "../data/model_output.txt"
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
		indices = pd.Series(self.df.index ,index=self.df['title']).drop_duplicates()
		idx = indices[title]
		sim_scores = list(enumerate(cosine_sim[idx]))
		sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
		sim_scores = sim_scores[1:11]
		movie_indices = [i[0] for i in sim_scores]
		return self.df['title'].iloc[movie_indices]


def main(title):
	recommendations = recSysContent().recommend(title=title)
	print(recommendations)
	return None


if __name__ == '__main__':
	title = sys.argv[1]
	main(title)

