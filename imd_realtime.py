import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
count = 0
stn = {}
df = pd.read_csv('clim_india_stn.csv')
la = df['lat'].tolist()
lo = df['lon'].tolist()
nm = df['name'].tolist()
idx =df['wmoid'].tolist()
lalo = [[str(float(x))+'_'+str(float(y)),z,l] for x,y,z,l in zip(la,lo,idx,nm)]
for item in lalo:
 if item[0] in stn.keys():
  stn[item[0]].append(item[1])
  stn[item[0]].append(item[2])
 else:
  stn[item[0]] = [item[1],item[2]]
keylist = stn.keys()
sorted(keylist)
names1 = []
rej = ['42699','42916','42475','43326','43351','42866','43327','42261','42354','42366','43259','42558','42555',
'42747','42451','43019','42122','42669','43299','42080','42727','42282','42977','42795','42471','42456','42799',
'42375','42055','42146','42920','43283']
for key in keylist:
 names1.append(stn[key][0])
 names1.append(stn[key][1])
#print(names1)
df1 = pd.read_csv('two.csv')
df1.columns = ['Name', 'val']
sl = df1['Name'].tolist()
df_actual = pd.DataFrame()
for i in range(len(sl)):
 if sl[i] in names1:
  j = names1.index(sl[i])
  sid = str(names1[j-1])
  if sid not in rej:
   url = "https://www.ogimet.com/cgi-bin/gsynres?lang=en&ind="+sid+"&ndays=30&ano=2024&mes=07&day=01&hora=03&ord=DIR&Send=Send"
   print(url)
   dfs = pd.read_html(url)
   date = dfs[2][('Date', 'Date')]
   rain = dfs[2][('Prec. (mm)', 'Prec. (mm)')]
   # concatenating the DataFrames 
   df2 = pd.concat([date, rain], join = 'outer', axis = 1)
   df_actual = pd.concat([df_actual,df2],axis=0)
   time.sleep(5)
   count+=1
   print(count)
print(df_actual)

