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
        if count == 6500:
            break
        if row[1] == 'Yes':
            value.append(row)
            neededdata.append(row)
            accepteddatacount+=1
        count+=1
       
with open("working_data/initialdata-without-no.csv","w") as fd:
    writer = csv.writer(fd, delimiter=",")
    writer.writerows(neededdata)
    
with open("working_data/initialdata-without-no.tsv","w") as fd:
    writer = csv.writer(fd, delimiter="\t", quotechar='"') #for tsv
    writer.writerows(neededdata)
