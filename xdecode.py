import xarray as xr
import numpy as np
import pandas as pd
import time
ds = xr.open_dataset("wonder_fc.nc")
keylist = ds.keys()
#print(keylist)
for key in keylist:
 # select a variable subset
 ds_sub = ds.get([str(key)])
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
 df4 = pd.read_csv('tp_spread.csv')
 df4_ = df4['tp']
 df3 = pd.concat([df3, df4_.rename("tpsp")], axis=1)
 print('mean and spread extracted....')
 df5 = df3.groupby(['latitude','longitude'])
 first=[]
 lat_=[]
 lon_=[]
 for item in df5:
  lat,lon = item[0]
  fname = str(lat)+'_'+str(lon)
  df6 = item[1]
  lat_.append(lat)
  lon_.append(lon)
  first.append(df6['tp'].values[0])
  df7 = df6['tp'].diff()
  df7 = round(df7*1000)
  df6 = pd.concat([df6, df7.rename("tp24")], axis=1)
  df6_ = df6[['latitude','longitude','valid_time','tp','tp24','tpsp','forecast_period','forecast_reference_time']]
  df6_.to_csv('./srf/'+fname+'.csv')
data = {'lat':lat_,'lon':lon_,'tp24':first}
df8 = pd.DataFrame.from_dict(data)
df8['tp24'] = round(df8['tp24']*1000)
df8.to_csv('one.csv')
#print(len(lat_),len(lon_),len(first))
print('done....')
