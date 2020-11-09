name = input('Enter file: ')
handle = open(name)

counts = dict()
for line in handle:
    if ( line.find("From ") != -1 ):
        dow = line.split()[2]
        counts[dow] = counts.get(dow,0) + 1

print(counts)
