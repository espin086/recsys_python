import pandas as pd 
import datetime


class IMDBMergedData:

	def __init__(self):
		self.metaData = pd.read_csv("../data/movies_metadata_clean.csv")
		self.keywords = pd.read_csv("../data/keywords_clean.csv")
		self.credits = pd.read_csv("../data/credits_clean.csv")
		self.location_clean = "../data/merged_clean.csv"
		self.current_time = datetime.datetime.now()
		pass
	
	def get_raw(self):
		df = self.metaData.merge(self.credits, on='id')
		df = df.merge(self.keywords, on='id')
		return df

	def clean_raw(self):
		df = self.get_raw()
		keep_vars = ['id','title', 'release_date', 
		'budget', 'revenue', 
		'runtime', 'genres', 
		'vote_count', 'vote_average', 
		'overview', 'cast', 'crew', 
		'director', 'keywords'
		]
		df = df[keep_vars]

		#removes spaces and converts to lowercase
		return df

	def save_clean(self):
		df = self.clean_raw()
		df['saved_on'] = self.current_time
		df = df.to_csv(self.location_clean, index=False)
		print("INFO: saved to {0}".format(self.location_clean))
		return None

	def get_clean(self):
		df = pd.read_csv(self.location_clean)
		return df



if __name__ == '__main__':
    IMDBMergedData().save_clean()
    print(IMDBMergedData().get_clean().head())



