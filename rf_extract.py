import pandas as pd
stn = {}
df = pd.read_csv('clim_india_stn.csv')
la = df['lat'].tolist()
lo = df['lon'].tolist()
nm = df['name'].tolist()
lalo = [[str(float(x))+'_'+str(float(y)),z] for x,y,z in zip(la,lo,nm)]
for item in lalo:
 if item[0] in stn.keys():
  stn[item[0]].append(item[1])
 else:
  stn[item[0]] = [item[1]]
keylist = stn.keys()
sorted(keylist)
import glob
count = 0
files = glob.glob('/home/dc/prog/srf/*.csv')
df1 = pd.DataFrame()
for file in files:
 pth = file.split('/')
 fp = pth[-1][:-4]
 if fp in keylist:
  df = pd.read_csv(file)
  name = stn[fp][0]
  df['dist'] = pd.Series([name for x in range(len(df.index))])
  df_ = df[['dist','valid_time','tp24','tpsp']]
  df1 = pd.concat([df1,df_], axis=0)
  count+=1
df2 = df1.groupby('valid_time')
df3 = pd.DataFrame()
for item in df2:
 df3 = pd.concat([df3,item[1]], axis=0)
df3.to_csv('wonder.csv')
print(count)

