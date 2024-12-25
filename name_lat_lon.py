import pandas as pd
df1 = pd.read_csv('wonder1.csv')
dst = df1['dist'].tolist()
df2 = pd.read_csv('clim_india_stn.csv')
la = df2['lat'].tolist()
lo = df2['lon'].tolist()
nm = df2['name'].tolist()
ids = df2['wmoid'].tolist()
fl = open('meta.csv','w+')
fl.write('district'+','+'wmoid'+'\n')
for i in range(len(dst)):
 if dst[i] in nm:
  fl.write(dst[i]+','+str(ids[i])+'\n')
fl.close()
