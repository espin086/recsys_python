import pandas as pd
import datetime

class DatasetTemplate:
	
	def __init__(self, raw_location, clean_location):
		self.raw_location = raw_location
		self.clean_location = clean_location
		self.current_time = datetime.datetime.now()
		self.current_date = datetime.datetime.now().date()

		print("""
		INFO: You have instantiated a DatasetTemplate OBJECT

		ATRIBUTES:
		----------------------
		raw_location = {0}
		clean_location = {1}

		METHODS:
		----------------------
		get_raw()
		clean_raw()
		get_clean()
		summarize()
		----------------------

			""".format(self.raw_location, self.clean_location))
		return None

	def get_raw(self):
		raw = pd.read_csv(self.raw_location)
		return raw

	def clean_raw(self):
		raw = self.get_raw()
		raw['current_time'] = self.current_time
		raw['current_date'] = self.current_date
		raw = raw.to_csv(self.clean_location, index=False)
		print("INFO: cleaned data saved to {0}".format(self.clean_location))
		return None

	def get_clean(self):
		clean = pd.read_csv(self.clean_location)
		return clean

	def summarize(self, raw_or_clean):
		summaries = {}
		if raw_or_clean == 'raw':
			print("INFO: RAW DATA summary ")
			df = pd.read_csv(self.raw_location)
		elif raw_or_clean == 'clean':
			print("INFO: CLEAN DATA summary")
			df = pd.read_csv(self.clean_location)
		
		print('-'* 30)
		print("INFO: df.isna().sum() for {0}".format(raw_or_clean))
		print(df.isna().sum())
		print('-'* 30)
		print("INFO: df.shape for {0}".format(raw_or_clean))
		print(df.shape)
		print('-'* 30)
		print("INFO: df.dtypes for {0}".format(raw_or_clean))
		print(df.dtypes)
		print('-'* 30)
		print("INFO: df.head() for {0}".format(raw_or_clean))
		print(df.head())
		print('-'* 30)
		print("INFO: df.describe()for {0}".format(raw_or_clean))
		print(df.describe())
		print('-'* 30)
		print("INFO: df.corr()for {0}".format(raw_or_clean))
		print(df.corr())
		print('-'* 30)
		return summaries





