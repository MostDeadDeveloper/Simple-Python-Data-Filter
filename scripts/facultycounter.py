# -*- coding: utf-8 -*- 585 586 

# -*- coding: utf-8 -*-

import csv
value = []
count = 1
neededdata=[]
allowed = 0 
testcount = 0 
accepteddatacount = 1 
with open("../working_data/initialdata-without-no.tsv") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    for row in rd:
        if row[1] == 'Yes':
            testcount+=1
            if row[3] =="Faculty" :
                row.insert(0,count)
                value.append(row)
                neededdata.append(row)
                accepteddatacount+=1
        count+=1
       
with open("../working_data/facultylist.tsv","w") as fd:
    writer = csv.writer(fd, delimiter="\t", quotechar='"') #for tsv
    #writer = csv.writer(fd, delimiter=",")
    writer.writerows(neededdata)
    
# -*- coding: utf-8 -*-
