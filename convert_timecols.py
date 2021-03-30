#!/usr/bin/env python
# coding: utf-8


import pandas as pd 


df = pd.read_csv("data_with_coord.csv", encoding='utf-8')


df = df[df.dist_euclidian < 150000]
df.drop(['Easting_rounded','Northing_rounded'], axis = 1, inplace = True)
month_to_number = {'janv' : '01','fevr':'02','mars':'03','avr':'04','mai':'05','juin':'06','juil':'07','aout':'08','sept':'09','oct':'10','nov':'11','dec':'12'}
def myfunc(d):
    splitted = d['DateOfCall'].split('-')
    if len(splitted)>1:
       date = splitted[0]+'/'+month_to_number[splitted[1]]+'/'+str(d.CalYear)
    else:
       date = splitted[0]
    d['TimeOfCall'] = pd.to_datetime(date+' '+d['TimeOfCall'], format="%d/%m/%Y %H:%M:%S")
    return d

from pandarallel import pandarallel
pandarallel.initialize(progress_bar=True, nb_workers=6)

df = df.parallel_apply(myfunc, axis=1)


import pickle
df.to_pickle('data_with_coord_29_03_21')  
#df = pd.read_pickle(file_name)
#df.to_csv(r'data_with_coord_1.csv', index = False)