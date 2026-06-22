import pandas as pd

# Read district lat/lon
with open('dist_lat_lon.csv') as fl:
    lines = [line.rstrip('\n') for line in fl]

dist = {}
for line in lines:
    #print(line)
    txt = line.split(',')
    dist[txt[0]] = [txt[1], txt[2]]  # lat, lon

# Read rainfall data
rows = []
countd = countn = counte = 0
with open('rf.csv') as f:
    lins = [ln.rstrip('\n') for ln in f]

for lin in lins:
    txt = lin.split(',')
    if len(txt) == 15 and txt[0].isdigit():
        rf = txt[10]
        name = txt[1]

        if name in dist:
            lat, lon = dist[name][0], dist[name][1]
            rows.append({"district": name, "lat": lat, "lon": lon, "rainfall": rf})
        else:
            print("Unknown district:", name, rf)

        # Count categories
        if 'D' in txt[11]:
            countd += 1
        elif 'N' in txt[11]:
            countn += 1
        elif 'E' in txt[11]:
            counte += 1
        else:
            print("Unclassified:", txt)

# Build DataFrame
df = pd.DataFrame(rows)

print(df)  # preview
tot = countd + countn + counte
print(countd, countn, counte, tot)
print(countd/tot, countn/tot, counte/tot)
