import csv

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
		numericalindex = 0
		found = "Undetected Value"
		for x in dictwordlist:
			numericalindex +=1
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

		# converts the data into numerical data at the end of the file for data analysis.
		if found == "Detected Value":
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

	return value


wordlist = {}
# How do you connect to the Internet? (Please check all applicable answers)? 24 : Student
testvalue = BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
            "studentlist.tsv",
            24,
            "MethodofConnectiontoTheInternet - STUDENT - Query",
            delimiterval="\t",
            counterresults_filename="MethodofConnectiontoTheInternet-student-counter_results.tsv",
            raw_counterresults_filename="raw-MethodofConnectiontoTheInternet-student-counter_results.tsv"
              )
