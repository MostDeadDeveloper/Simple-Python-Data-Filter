import csv

dictwordlist = {}
source_filename = "studentlist.tsv"
row_index = 24
queryname = "Default Query"

delimiterval="\t"
counterresults_filename="default-counter_results.tsv"
raw_counterresults_filename="raw_default-counter_results.tsv"


# from Counter import MultipleResultsCounter_self_aware_dictionary_and_output_Numerical_Data

# wordlist = {}
# MultipleResultsCounter_self_aware_dictionary_and_output_Numerical_Data(
# 	wordlist,
# 	"studentlist.tsv",
# 	23,
# 	"TestingDAta - STUDENT - Query",
# 	delimiterval="\t",
# 	counterresults_filename="TestingDAta-student-counter_results.tsv",
# 	raw_counterresults_filename="raw-TestingDAta-student-counter_results.tsv"
# )

value = []
totalcount = 0
with open("../working_data/"+source_filename) as fd:
	rd = csv.reader(fd, delimiter=delimiterval, quotechar='"')
	for row in rd:
		value.append(row)
		totalcount+=1

wordlistrecords = list(dictwordlist)
casefound = 0
numericalindex = 1
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
