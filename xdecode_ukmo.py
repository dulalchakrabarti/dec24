import xarray as xr
import numpy as np
import pandas as pd
ds = xr.open_dataset("wonder_fc.nc")
keylist = ds.keys()
#print(keylist)
for key in keylist:
 # select a variable subset
 ds_sub = ds.get([str(key)])
 df1 = ds_sub.to_dataframe()
 df1.to_csv(str(key)+'.csv')
print('done...')
'''
 ds_mean = ds_sub.mean(dim='number')
 ds_std = ds_sub.std(dim='number')
 #Convert to pandas dataframe and save it
 df1 = ds_mean.to_dataframe()
 #print(df1)
 df2 = ds_std.to_dataframe()
 #print(df2)
 df1.to_csv(str(key)+'_mean.csv')
 df2.to_csv(str(key)+'_spread.csv')
 df3 = pd.read_csv('tp_mean.csv')
 #print(df3)
 df4 = pd.read_csv('tp_spread.csv')
 #print(df4)
 df5 = df3.groupby(['latitude','longitude'])
 for item in df5:
  lat,lon = item[0]
  fname = str(lat)+'_'+str(lon)
  df6 = item[1]
  df7 = df6['tp'].diff()
  df8 = round(df7*1000)
  ldf8 = df8.tolist()
  df9 = df6.assign(tp_diff = ldf8)
  df9.to_csv('./srf/'+fname+'.csv')
'''
