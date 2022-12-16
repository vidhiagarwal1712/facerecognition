import csv
from datetime import date
dataset1 = []
dataset2 = []
with open('Data Merging/dataset_1.csv','r') as f:
    csvreader = csv.reader(f)
    for g in csvreader:
        dataset1.append(g)
header1 = dataset1[0]
planetdata1 = dataset1[1:]
with open('Data Merging/dataset_2.csv','r') as f:
    csvreader = csv.reader(f)
    for g in csvreader:
        dataset2.append(g)
header2 = dataset2[0]
planetdata2 = dataset2[1:]

finalheader = header1+header2
print(len(planetdata1))
print(len(planetdata2))
finalplanetdata = []
for f in range(0,len(planetdata1)):
    finalplanetdata.append(planetdata1[f]+planetdata2[f])
for f in range(len(planetdata1),len(planetdata2)):
    finalplanetdata.append(planetdata2[f])
with open('finaldataset.csv','a+',newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(finalheader)
    csvwriter.writerows(finalplanetdata)