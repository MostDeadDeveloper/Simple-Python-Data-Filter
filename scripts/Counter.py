# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import csv
def BaseCounter(
                dictwordlist,
                source_filename,
                row_index,
                queryname="Current Query",
                delimiterval="\t",
                counterresults_filename="default-counter_results.tsv",
                raw_counterresults_filename="raw_default-counter_results.tsv"
                ):
    value = []
    totalcount = 0 
    with open("../working_data/"+source_filename) as fd:
        rd = csv.reader(fd, delimiter=delimiterval, quotechar='"')
        for row in rd:
            value.append(row)
            totalcount+=1
            
    
    #wordlist = {"anonas":0,"de dios":0,"luisa":0,"mulawin":0,"duhat":0}
    #x = 1
    casefound = 0
    for z in value:
        found = "Undetected Value"
        for x in dictwordlist:
            if x.lower() in z[row_index].lower():
                dictwordlist[x]+=1
                casefound+=1
                break
                
        z.append(found)
        
    with open("../Output-Results/RawCounterResults/"+raw_counterresults_filename,"w") as fd:
        writer = csv.writer(fd, delimiter="\t", quotechar='"')
        writer.writerows(value)
    with open("../Output-Results/CounterResults/"+counterresults_filename,"w") as fd:
        writer = csv.writer(fd, delimiter="\t", quotechar='"')
        writer.writerow([dictwordlist])
    
    
    #display all results:
    print("\n{} Query Results:".format(queryname))
    print("Found Cases : {} , out of {}".format(casefound,totalcount))
    print(dictwordlist)
    
def getWordListFromFile(dictwordlist_filename):
    dictwordlist = {}
    with open("../dictlist/"+dictwordlist_filename) as fd:
        temp = fd.read().splitlines()
        for x in temp:
            dictwordlist[x.lower()] = 0
    return dictwordlist
def BaseCounter_and_TransferTo_WorkingData(dictwordlist,
                                            source_filename,
                                            row_index,
                                            queryname="Current Query",
                                            delimiterval="\t",
                                            counterresults_filename="default-counter_results.tsv",
                                            raw_counterresults_filename="raw_default-counter_results.tsv"
                                            ):
    value = []
    totalcount =0 
    with open("../working_data/"+source_filename) as fd:
        rd = csv.reader(fd, delimiter=delimiterval, quotechar='"')
        for row in rd:
            value.append(row)
            totalcount+=1
    
    #wordlist = {"anonas":0,"de dios":0,"luisa":0,"mulawin":0,"duhat":0}
    x = 1
    casefound = 0
    for z in value:
        found = "Undetected Value"
        for x in dictwordlist:
            if x.lower() in z[row_index].lower():
                dictwordlist[x]+=1
                casefound+=1
                break
                
        z.append(found)
        
    with open("../working_data/"+raw_counterresults_filename,"w") as fd:
        writer = csv.writer(fd, delimiter="\t", quotechar='"')
        writer.writerows(value)
    with open("../Output-Results/CounterResults/"+counterresults_filename,"w") as fd:
        writer = csv.writer(fd, delimiter="\t", quotechar='"')
        writer.writerow([dictwordlist])

    #display all results:
    print("\n{} Query Results:".format(queryname))
    print("Found Cases : {} , out of {}".format(casefound,totalcount)) 
    print(dictwordlist)
