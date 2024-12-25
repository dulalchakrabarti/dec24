import pandas as pd
import time
df1 = pd.read_csv('wonder.csv')
dl = df1['dist'].tolist()
df2 = pd.read_csv('meta.csv')
names = df2['district'].tolist()
ids = df2['wmoid'].tolist()
df3 = pd.read_csv('frames.csv')
stn = {}
for name in names:
 idx = names.index(name)
 stn[name] = str(ids[idx])
count = 0
df4 = pd.DataFrame()
for item in dl:
 dn = item
 wid = stn[item]
 df3_ = df3[(df3['fname'] == int(wid)) & (df3['date'] >'2024-06-01') & (df3['date']<'2024-09-30')]
 df4 = pd.concat([df4,df3_], axis=0)
 count+=1
 print(count,'....item added in data frame')
 time.sleep(3)
print(count) 
df4.to_csv('new.csv')
