#!/usr/bin/env python
# coding: utf-8


import pandas as pd 
import pickle
df = pd.read_pickle('data_with_coord_29_03_21')
#df = pd.read_csv("data_with_coord.csv", encoding='utf-8').tail(300000)

def myfunc2(d):
    if len(d['TimeMobile'])<17: d['TimeMobile']=d['TimeMobile']+':00'
    if len(d['TimeArrived'])<17: d['TimeArrived']=d['TimeArrived']+':00'
    if len(d['TimeMobilised'])<17: d['TimeMobilised']=d['TimeMobilised']+':00'
    d['TimeMobile'] = pd.to_datetime(d['TimeMobile'], format="%d/%m/%Y %H:%M:%S")	
    d['TimeArrived'] = pd.to_datetime(d['TimeArrived'], format="%d/%m/%Y %H:%M:%S")
    d['TimeMobilised'] = pd.to_datetime(d['TimeMobilised'], format="%d/%m/%Y %H:%M:%S")
    return d
from pandarallel import pandarallel
pandarallel.initialize(progress_bar=True, nb_workers=6)

df = df.parallel_apply(myfunc2, axis=1)
df['ResponseTime'] = (df.TimeArrived-df.TimeOfCall).astype('timedelta64[s]')

df.to_pickle('data_with_coord_29_03_21')  
#df = pd.read_pickle(file_name)
#df.to_csv(r'data_with_coord_1.csv', index = False)