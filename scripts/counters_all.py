# -*- coding: utf-8 -*- 585 586 

# -*- coding: utf-8 -*-

from Counter import (BaseCounter,
                    getWordListFromFile,
                    BaseCounter_and_TransferTo_WorkingData)

"""
def BaseCounter(
                dictwordlist,
                source_filename,
                row_index,
                queryname="Current Query",
                delimiterval="\t",
                counterresults_filename="default-counter_results.tsv",
                raw_counterresults_filename="raw_default-counter_results.tsv"
                ):
"""
#Student Counter
wordlist = {"student":0}
BaseCounter_and_TransferTo_WorkingData(wordlist,
            "initialdata-without-no.tsv",
            4,
            queryname="Student Query",
            delimiterval="\t",
            counterresults_filename="student_counter_results.tsv",
            raw_counterresults_filename="studentlist.tsv"
            )



#FAculty  Counter
wordlist = {"faculty":0}
BaseCounter(
            wordlist,
            "initialdata-without-no.tsv",
            4,
            queryname="Faculty Query",
            delimiterval="\t",
            counterresults_filename="faculty_counter_results.tsv",
            raw_counterresults_filename="raw_faculty-counter_results.tsv"
            )

# Access To Technology -Counter 
wordlist = {"yes":0,"no":0}
BaseCounter(wordlist,
            "studentlist.tsv",
            14
            ,
            "Access To Technology Query",
            delimiterval="\t",
            counterresults_filename="access_to_technology_counter_results.tsv",
            raw_counterresults_filename="raw_access_to_technology-counter_results.tsv"
            )

# College_Branches_Campuses Counter 
wordlist = getWordListFromFile("collegebranchcampus-list.txt")
BaseCounter(wordlist,
            "studentlist.tsv",
            3,
            "College_Branches_Campuses Query",
            delimiterval="\t",
            counterresults_filename="college_branches_campuses_counter_results.tsv",
            raw_counterresults_filename="raw_college_branches_campuses-counter_results.tsv"
            )

# Computer OS Counter
wordlist = {"windows":0,"mac os":0,"linux":0,"Mac OS":0}
BaseCounter(wordlist,
            "studentlist.tsv",
            15,
            "Computer_OS Query",
            delimiterval="\t",
            counterresults_filename="computeros_results.tsv",
            raw_counterresults_filename="raw_computeros-counter_results.tsv"
            )

# Course List Counter
wordlist = getWordListFromFile("courselist.txt")
BaseCounter(wordlist,
            "studentlist.tsv",
            8,
            "Course Query",
            delimiterval="\t",
            counterresults_filename="coureslist_results.tsv",
            raw_counterresults_filename="raw_coureslist-counter_results.tsv"
            )


# Frequency of Computer Usage Counter
wordlist = getWordListFromFile("frequency_of_use_of_computers-list.txt")
BaseCounter(wordlist,
            "studentlist.tsv",
            16,
            "Frequency of Computer Usage Query",
            delimiterval="\t",
            counterresults_filename="frequency_of_use_of_computers_results.tsv",
            raw_counterresults_filename="raw_frequency_of_use_of_computers-counter_results.tsv"
             )
