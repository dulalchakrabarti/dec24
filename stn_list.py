fl = open('clim_fc.csv','w+')
stn = {}
lines = [line.rstrip() for line in open('clim_ncep.csv')]
fl.write('lat'+','+'lon'+','+'name'+','+'wmoid'+'\n')
for line in lines:
 line = line.split(',')
 if line[-1].isdigit():
  lat = int(float(line[1]))
  lon = int(float(line[2]))
  name = line[4]
  name_ = name[0]+name[1:].lower()
  wmoid = line[-1]
  buf = str(lat)+','+str(lon)+','+name_+','+line[-1]
  fl.write(buf+'\n')
  print(line)

