import requests
x = requests.get('https://www.tropmet.res.in/data/data-archival/rain/iitm-regionrf.txt')
buf = x.text
buf = buf.split('/n')
for i in buf:
 i = i.split('  ')
 print(i)

