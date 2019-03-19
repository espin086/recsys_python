import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import MovieLensData 

def build_test_and_train(X, y,test_size):
	data_x = X.copy()
	data_y = X[y]
	x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, stratify=data_y,test_size=test_size,random_state=42)
	return x_train, x_test, y_train, y_test

def rmse(y_true, y_pred):
	return np.sqrt(mean_squared_error(y_true, y_pred))

def baseline(user_id, movie_id):
	return 3

def score(cf_model, user_id, item_id, rating):
	#construct a list of user-movie tuples from the testing dataset
	id_pairs = zip(x_test[user_id], x_test[item_id])
	y_pred = np.array([cf_model(user,movie) for (user, movie) in id_pairs])
	#extract actual ratings data
	y_true = np.array(x_test[rating])
	#return final MSE score
	return rmse(y_true, y_pred)




if __name__ == '__main__':
	movie_lens = MovieLensData.MovieLensData()
	ratings = movie_lens.get_ratings()
	x_train, x_test, y_train, y_test = build_test_and_train(X=ratings, y='user_id', test_size=.25)
	score = score(baseline, user_id='user_id', item_id='movie_id', rating='rating')
	print(score)









