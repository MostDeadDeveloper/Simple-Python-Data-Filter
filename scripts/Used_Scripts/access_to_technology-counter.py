    # -*- coding: utf-8 -*-

import csv
value = []
with open("../working_data/studentlist.tsv") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    for row in rd:
        value.append(row)

streetwordlist = {"yes":0,"no":0}
foodcounter = 0 
place = 1
#streetwordlist = {"anonas":0,"de dios":0,"luisa":0,"mulawin":0,"duhat":0}
x = 1
casefound = 0 
for z in value:
    found = "Undetected Value"
    for x in streetwordlist:
        if x in z[15].lower():
            found = "Detected Answer"
            streetwordlist[x]+=1
            casefound+=1
            break
    z.append(found)
    #if found == "Detected Course":
    #    z.append(x)
    #else:
    #    z.append("Undetected Value")
        
        
    
with open("../Output-Results/RawCounterResults/raw-access_to_technology-results.tsv","w") as fd:
    writer = csv.writer(fd, delimiter="\t", quotechar='"')
    writer.writerows(value)
with open("../Output-Results/CounterResults/access_to_technology-count.tsv","w") as fd:
    writer = csv.writer(fd, delimiter="\t", quotechar='"')
    writer.writerow([streetwordlist])

"""
if z[2] in i[1].lower():
            found = "DETECTED STREET BY MACHINEEEE"
            foodcounter+=1
            break
    results.append([x,found])
    x+=1
"""# -*- coding: utf-8 -*-

