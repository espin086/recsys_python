import pandas as pd 

metaData = pd.read_csv("../data/movies_metadata_clean.csv")
keywords = pd.read_csv("../data/keywords_clean.csv")
credits = pd.read_csv("../data/credits_clean.csv")
df = metaData.merge(credits, on='id')
df = df.merge(keywords, on='id')

keep_vars = ['id','title', 'release_date', 
	'budget', 'revenue', 
	'runtime', 'genres', 
	'vote_count', 'vote_average', 
	'overview', 'cast', 'crew', 
	'director', 'keywords'
]

df = df[keep_vars]

print(df.head())



