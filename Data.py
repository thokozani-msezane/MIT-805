#The following code helps woth ingestion of the dataset into a combined dataframe in Python using NUMPY
#The code is freely available on Kaggle and will form the base of the pre processing of the dataset
#Reference BwandoWando. (2023). <i>(🌇Sunset) 🇺🇦 Ukraine Conflict Twitter Dataset </i>[Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DSV/5934908


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os, csv, gc
from pathlib import Path 

csv_collection = []
for dirname, _, filenames in os.walk('/kaggle/input'):
    filenames.sort()
    for filename in filenames:
        fullpath = os.path.join(dirname, filename)
        csv_collection.append(fullpath)



columns = ["tweetcreatedts","extractedts","tweetid"]

csv_collection.sort()
dataframe_collection = []
for csvfile in csv_collection:
    df = pd.read_csv(csvfile, engine='python', compression='gzip',encoding='utf-8', quoting=csv.QUOTE_ALL, usecols=lambda x: x in columns)
    dataframe_collection.append(df)

df = None
del df
gc.collect()

df_combined = pd.concat(dataframe_collection, axis=0)
df_combined['tweetcreatedts'] = pd.to_datetime(df_combined['tweetcreatedts'], errors='coerce')
df_combined['extractedts'] = pd.to_datetime(df_combined['extractedts'], errors='coerce') 
df_combined.reset_index(inplace=True, drop=True)

dataframe_collection = None
del dataframe_collection
gc.collect()

df_combined.shape

