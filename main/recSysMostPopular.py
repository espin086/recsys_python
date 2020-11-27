import pandas as pd
import numpy as np
import datetime


class recSysIMDBTop250:
	def __init__(self,location_clean, avg_metric, count_metric):
		self.location_clean = location_clean
		self.avg_metric = avg_metric
		self.count_metric = count_metric
		self.current_time = datetime.datetime.now()

	def get_imdb_recsys(self):
		df = pd.read_csv(self.location_clean)
		m = df[self.count_metric].quantile(0.99)
		df = df[df[self.count_metric] >= m]
		C = df[self.avg_metric].mean()
		def weighted_rating(df, m=m, C=C):
			v = df[self.count_metric]
			R = df[self.avg_metric]
			return (v/(v+m) * R) + (m/(m+v) * C)
		df['score'] = df.apply(weighted_rating, axis=1)
		df = df.sort_values(by='score', ascending=False)
		df = df[['title','score']].head(n=10)

		return df


if __name__ == '__main__':
 
    recommendation = recSysIMDBTop250(
    	location_clean="../data/merged_clean.csv", 
    	avg_metric='vote_average', 
    	count_metric='vote_count').get_imdb_recsys()
    print('*' * 80)
    print("YOUR MOVIE RECOMMENDATIONS")
    print('*' * 80)
    print(recommendation.to_string(index=False))
    print('*' * 80)
	