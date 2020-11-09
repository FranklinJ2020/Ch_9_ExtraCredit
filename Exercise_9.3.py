name = input('Enter file: ')
handle = open(name)

counts = dict()
for line in handle:
    if ( line.find("From ") != -1 ):
        femail = line.split()[1]
        counts[femail] = counts.get(femail,0) + 1

print(counts)
