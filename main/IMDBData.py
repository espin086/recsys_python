
# coding: utf-8

# In[75]:


import pandas as pd
import numpy as np
import datetime


# In[111]:


class IMDBData:
    def __init__(self):
        self.location_raw = "../data/movies_metadata.csv"
        self.location_clean = "../data/movies_metadata_clean.csv"
        self.current_time = datetime.datetime.now()
        pass
    
    def get_raw(self):
        raw = pd.read_csv(self.location_raw)
        return raw
    
    def clean_raw(self):
        raw = self.get_raw()
        #filtering by select variables
        keep_vars = ['title', 'release_date', 
                          'budget', 'revenue', 
                          'runtime', 'genres', 
                          'vote_count', 'vote_average', 'overview'
                         ]
        narrow = raw[keep_vars]
        #converting datatypes
        def to_float(x):
            try:
                x = float(x)
            except:
                x = np.nan
            return x
        narrow['budget'] = narrow['budget'].apply(to_float)
        #convert release_date into into pandas dataframe
        narrow['release_date'] = pd.to_datetime(narrow['release_date'], errors='coerce')
        #extract year from the datetime
        narrow['year'] = narrow['release_date'].apply(lambda x: str(x).split('-')[0] if x != np.nan else np.nan)
        narrow = narrow[(narrow['runtime'] >= 45) & (narrow['runtime'] <= 300)]
        return narrow
    
    def save_clean(self):
        df = self.clean_raw()
        df['saved_on'] = self.current_time
        df = df.to_csv(self.location_clean, index=False)
        print("INFO: saved to {0}".format(self.location_clean))
        return None
    
    def get_clean(self):
        df = pd.read_csv(self.location_clean)
        return df
    
    def summarize(self, dataset):
        summary_dict = {}
        if dataset == 'raw':
            df = self.get_raw()
        elif dataset == 'clean':
            df = self.get_clean()
        summary_dict['describe'] = df.describe()
        return summary_dict


# In[116]:


def main():
    main_dict = {}
    main_dict['raw_data'] = IMDBData().get_raw()
    main_dict['raw_summary'] = IMDBData().summarize(dataset='raw')
    main_dict['clean_summary'] = IMDBData().summarize(dataset='clean')
    main_dict['clean_data'] = IMDBData().get_clean()
    print("INFO: dictionary returned with the following datasets")
    print(main_dict.keys())
    
    return main_dict


# In[118]:

if __name__ == '__main__':
    IMDBData().save_clean()



# In[ ]:




