import numpy as np

#converting datatypes
def to_float(x):
    try:
        x = float(x)
    except:
        x = np.nan
    return x

def to_int(x):
    try:
        return int(x)
    except:
        return np.nan


def generate_list(x):
	if isinstance(x, list):
		names = [ele['name'] for ele in x]
		#if list greater than 3 return only top 3, else return entire list
		if len(names) > 3:
			names = names[:3]
		return names
	# if instance is not a list or is malformed, then return an empty list
	return []