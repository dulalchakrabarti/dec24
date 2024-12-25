lines = [ line.rstrip() for line in open('acc.csv')]
fl = open('err.csv','w+')
for line in lines:
 line = line.split(',')
 line = line[:6]
 buf = ','.join(str(x) for x in line)
 print(buf)
 fl.write(buf+'\n')
fl.close()
