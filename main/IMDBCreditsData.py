import pandas as pd
import numpy as np
import datetime
from ast import literal_eval
import Utilities.DataTransforms as UtilitiesDataTransforms
import Utilities.DatasetTemplate as DatasetTemplate



class IMDBCreditsData(DatasetTemplate.DatasetTemplate):
	def __init__(self, raw_location, clean_location):
		 DatasetTemplate.DatasetTemplate.__init__(self, raw_location, clean_location)


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
		raw['current_time'] = self.current_time
		raw['current_date'] = self.current_date
		raw = raw.to_csv(self.clean_location, index=False)
		print("INFO: saved to {0}".format(self.clean_location))
		return None



if __name__ == '__main__':
	IMDBCreditsData = IMDBCreditsData(raw_location="../data/credits.csv", clean_location="../data/credits_clean.csv")
	# IMDBCreditsData.clean_raw()
	IMDBCreditsData.summarize(raw_or_clean='clean')
	
	





