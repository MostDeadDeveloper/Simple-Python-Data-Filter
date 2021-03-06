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

	casefound = 0
	for z in value:
		found = "Undetected Value"
		for x in dictwordlist:
			if x.lower() in z[row_index].lower():
				found = "Detected Value"
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
	finalvalues = []
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
				finalvalues.append(z)
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

def BaseCounter_self_aware_dictionary(
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

	casefound = 0
	for z in value:
		found = "Undetected Value"
		for x in dictwordlist:
			if x.lower() in z[row_index].lower():
				found = "Detected Value"
				dictwordlist[x]+=1
				casefound+=1
				break

		# adds it to the dictlist if it is a new kind of word, and if the string word is not empty.
		if ((found == "Undetected Value")and(z[row_index].lower() != '')):
			dictwordlist[z[row_index].lower()] = 1
			casefound+=1


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



def BaseCounter_self_aware_dictionary_and_output_Numerical_Data(
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

	casefound = 0
	for z in value:
		numericalindex = 1
		found = "Undetected Value"
		for x in dictwordlist:
			if x.lower() in z[row_index].lower():
				found = "Detected Value"
				dictwordlist[x]+=1
				casefound+=1
				break
			numericalindex +=1

		# adds it to the dictlist if it is a new kind of word, and if the string word is not empty.
		if ((found == "Undetected Value")and(z[row_index].lower() != '')):
			dictwordlist[z[row_index].lower()] = 1
			casefound+=1


		z.append(found)

		# converts the data into numerical data at the end of the file for data analysis.
		if z[row_index].lower() != '':
			z.append(numericalindex)
		else:
			z.append(0)


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



# BaseCounterFilter removes from the sourcefile rows that does not have the words from the dictlist.
def BaseCounterFilter_and_TransferTo_WorkingData(dictwordlist,
										   source_filename,
										   row_index,
										   queryname="Current Query",
										   delimiterval="\t",
										   counterresults_filename="default-counter_results.tsv",
										   raw_counterresults_filename="raw_default-counter_results.tsv"
									   ):
	value = []
	finalvalues = []
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
				finalvalues.append(z)
				break

	with open("../working_data/"+raw_counterresults_filename,"w") as fd:
		writer = csv.writer(fd, delimiter="\t", quotechar='"')
		writer.writerows(finalvalues)
	with open("../Output-Results/CounterResults/"+counterresults_filename,"w") as fd:
		writer = csv.writer(fd, delimiter="\t", quotechar='"')
		writer.writerow([dictwordlist])

    #display all results:
	print("\n{} Query Results:".format(queryname))
	print("Found Cases : {} , out of {}".format(casefound,totalcount))
	print(dictwordlist)

def MultipleResultsCounter_self_aware_dictionary_and_output_Numerical_Data(
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

	wordlistrecords = list(dictwordlist)
	casefound = 0
	for z in value:

		if casefound == totalcount:
			break

		results =""
		allfounds = ""
		seperatedwordlist = z[row_index].split(";")

		for v in seperatedwordlist: # loop inside the multiple value answers
			if v.lower() != "":
				if v.lower() not in wordlistrecords: # if the current value matches the one in the dictionary
					wordlistrecords.append(v.lower())
					allfounds += "New Entry;"
					dictwordlist[v.lower()] = 1
					results+=str(wordlistrecords.index(v.lower())+1)+";"
				else:
					dictwordlist[v.lower()]+=1
					allfounds += "Existing Record;"
					results+=str(wordlistrecords.index(v.lower())+1)+";"
			else:
				allfounds += "Undetected Value;"
				results+="0;"

		casefound+=1
		z.append(allfounds)
		z.append(results)

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