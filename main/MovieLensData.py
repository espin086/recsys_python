
import pandas as pd
class MovieLensData:
	def __init__(self):
		self.location_raw = "../data/movielens"


	def get_users(self):
		keep_vars = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
		users = pd.read_csv('{0}/u.user'.format(self.location_raw), sep="|",\
			names=keep_vars,\
			encoding='latin-1'
			)
		return users

	def get_items(self, model_type='collaborative_filter'):
		keep_vars = ['movie_id', 'title', 'release_date', 'video release date', 'IMDb URL',\
				'unknown', 'Action', 'Adventure', 'Animation', "Children\'s", 'Comedy', 'Crime',\
				'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical','Mystery',\
				'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western'
			]

		items = pd.read_csv("{0}/u.item".format(self.location_raw), sep='|', names=keep_vars, encoding='latin-1')
		if model_type == 'collaborative_filter':
			items = items[['movie_id', 'title']]
		return items

	def get_ratings(self):
		keep_vars = ['user_id', 'movie_id', 'rating']
		ratings = pd.read_csv("{0}/u.data".format(self.location_raw), sep='\t', names=keep_vars, encoding='latin-1')
		return ratings



if __name__ == '__main__':
	MovieLensData().get_ratings()