import pandas as pd
df = pd.read_csv('wonder.csv')
df_ = df[df['valid_time'] == '2024-06-02']
names = df_['dist'].tolist()
#print(names)
df1 = pd.read_csv('one.csv')
la1 = df1['lat'].tolist()
lo1 = df1['lon'].tolist()
vl1 = df1['tp24'].tolist()
lalo1 = [[str(float(x))+'_'+str(float(y)),z] for x,y,z in zip(la1,lo1,vl1)]
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
names1 = []
vals1 = []
count = 0
for item in lalo1:
  if item[0] in keylist:
   names1.append(stn[item[0]][0])
   vals1.append(item[1])
   count+=1
fl = open('two.csv','w+')
for i in range(len(names)):
 if names[i] in names1:
  print (names[i],vals1[i])
  fl.write(names[i]+','+str(vals1[i])+'\n')
print(count)

