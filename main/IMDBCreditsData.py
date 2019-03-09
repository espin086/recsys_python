import pandas as pd
import numpy as np
import datetime
from ast import literal_eval
import Utilities.DataTransforms as UtilitiesDataTransforms


class IMDBCreditsData:
	def __init__(self):
		self.location_raw = "../data/credits.csv"
		self.location_clean= "../data/credits_clean.csv"
		self.current_time = datetime.datetime.now()

	def get_raw(self):
		raw = pd.read_csv(self.location_raw)
		return raw

	def clean_raw(self):
		raw = self.get_raw()
		#convert a string looking python object into actual python object
		features = ['cast', 'crew']
		for feature in features:
			raw[feature] = raw[feature].apply(literal_eval)

		def get_director(x):
			for crew_member in x:
				if crew_member['job'] == 'Director':
					return crew_member['name']
			return np.nan

		raw['director'] = raw['crew'].apply(get_director)
		raw['cast'] = raw['cast'].apply(UtilitiesDataTransforms.generate_list)
		clean = raw
		return clean

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
	IMDBCreditsData().save_clean()
	print(IMDBCreditsData().get_clean().head())