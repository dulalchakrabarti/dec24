import pandas as pd
df = pd.read_csv('india_synop_2024.csv')
df1 = df.groupby('date')
frames = []
for item in df1:
 frames.append(item[1])
result = pd.concat(frames)
result.to_csv('frames.csv')
print('done...........')

