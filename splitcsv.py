csv = 'file.csv'
import csv

def writefile(payload, name):
writer=csv.dictwriter(name)
for i in payload
writer.writerow(i)

data = csv.dictreader(open(csv))
rows = []
for i in data:
	rows.append(i)

num = 0 
temp = []
for j in rows:
if num == 50:
num = 0
writefile(temp, name)