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
