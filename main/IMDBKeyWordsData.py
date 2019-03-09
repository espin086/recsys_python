import pandas as pd
import numpy as np
import datetime
from ast import literal_eval
import Utilities.DataTransforms as UtilitiesDataTransforms


class IMDBKeyWordsData:
	def __init__(self):
		self.location_raw = "../data/keywords.csv"
		self.location_clean= "../data/keywords_clean.csv"
		self.current_time = datetime.datetime.now()

	def get_raw(self):
		raw = pd.read_csv(self.location_raw)
		return raw

	def clean_raw(self):
		raw = self.get_raw()
		#convert a string looking python object into actual python object
		features = ['keywords']
		for feature in features:
			raw[feature] = raw[feature].apply(literal_eval)
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
	IMDBKeyWordsData().save_clean()
	print(IMDBKeyWordsData().get_clean().head())