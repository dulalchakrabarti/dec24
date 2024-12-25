import pandas as pd
lines = [line for line in open('india_stn1.csv')]
for line in lines:
 line = line.split(',')
ids = line[:-1]
yr = list(range(2024,2025))
frames = []
for y in yr:
 for j in ids:
  y1 = str(y)
  wid = str(j)
  url = "https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/"+y1+"/"+j
  print(url)
  try:
   df = pd.read_csv(url)
   print('dowloaded.....',url)
   df1 = pd.DataFrame.from_dict({'fname':[j[:5]]*len(df.index),'date':df['DATE'].tolist(),'prcp':df['PRCP'].tolist(),'slp':df['SLP'].tolist(),'temp':df['TEMP'].tolist(),'dewp':df['DEWP'].tolist()})
  except:
   continue
  print(df1)
  frames.append(df1)
result = pd.concat(frames)
result.to_csv('india_synop_2024.csv')
print('done...........')

