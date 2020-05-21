# -*- coding: utf-8 -*-

import csv
value = []
count = 1
neededdata=[]
allowed = 0
accepteddatacount = 1
with open("originaldata.csv") as fd:
    rd = csv.reader(fd, delimiter=",", quotechar='"')
    for row in rd:
        value.append(row)
        #if count == 6500:
        #    break
        if row[1] == 'Yes':
            neededdata.append(row)
            accepteddatacount+=1
        count+=1

records = neededdata
# duplicates = []
# neededdata.sort()
# z = 0
# while(z != len(neededdata)-1):
#     if neededdata[z][2] == neededdata[z+1][2]:
#         duplicates.append([z,neededdata[z+1]])
#         neededdata.pop(z+1)
#     z+=1


with open("working_data/initialdata-without-no.csv","w") as fd:
    writer = csv.writer(fd, delimiter=",")
    writer.writerows(neededdata)

with open("working_data/initialdata-without-no.tsv","w") as fd:
    writer = csv.writer(fd, delimiter="\t", quotechar='"') #for tsv
    writer.writerows(neededdata)
#  'What operating system does your computer desktop, laptop/netbook have?' [16]
# 'In a weekly basis, how often do you use your computer desktop, laptop/netbook?' [17]