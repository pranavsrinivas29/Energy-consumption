import sys
import os
import pandas as pd
# Dynamically add the root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import config  # Now import config

class Pipeline:
    def __init__(self):
        pass

    def load(self):
        """Loads all datasets as Pandas DataFrames."""
        self.df_continent = pd.read_csv(config.DATA_PATHS["continent"])
        self.df_country = pd.read_csv(config.DATA_PATHS["country"])
        self.df_non_renewable = pd.read_csv(config.DATA_PATHS["non_renewable"])
        self.df_renewable = pd.read_csv(config.DATA_PATHS["renewable"])
        self.df_tot_power_gen = pd.read_csv(config.DATA_PATHS["tot_power_gen"])
        self.df_top_20 = pd.read_csv(config.DATA_PATHS["top_20"])
        
        #return self  # Return the instance for method chaining


if __name__ == '__main__':
    pipe = Pipeline()
    pipe.load()
    #df_continent = pipe.df_continent
    #print(df_continent.head(3))
    
    df_country = pipe.df_country
    print(df_country.head(3))
    print('NA counts: ', df_country.isna().any().sum())