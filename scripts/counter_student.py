# -*- coding: utf-8 -*-


from Counter import (BaseCounter,
                    getWordListFromFile,
                    BaseCounter_and_TransferTo_WorkingData,
					BaseCounter_self_aware_dictionary,
					BaseCounter_self_aware_dictionary_and_output_Numerical_Data,
				)

"""
def BaseCounter(
                dictwordlist,
                source_filename,
                row_index,
                queryname="Current Query",
                delimiterval="\t",
                counterresults_filename="default-counter_results.tsv",
                raw_counterresults_filename="raw-default-counter_results.tsv"
                ):
"""


# # College_Branches_Campuses Counter
# wordlist = {} #etWordListFromFile("collegebranchcampus-list.txt")
# BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
#             "studentlist.tsv",
#             3,
#             "College_Branches_Campuses - STUDENT - Query",
#             delimiterval="\t",
#             counterresults_filename="college_branches_campuses_counter_results.tsv",
#             raw_counterresults_filename="raw-college_branches_campuses-counter_results.tsv"
#             )

# # Course List Counter
# wordlist = getWordListFromFile("courselist.txt")
# BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
#             "studentlist.tsv",
#             8,
#             "Course - STUDENT - Query",
#             delimiterval="\t",
#             counterresults_filename="coureslist-student-_results.tsv",
#             raw_counterresults_filename="raw-coureslist-student-counter_results.tsv"
#             )


# # Access To Technology -Counter
# wordlist = {"yes":0,"no":0}
# BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
#             "studentlist.tsv",
#             14
#             ,
#             "Access To Technology- STUDENT - Query",
#             delimiterval="\t",
#             counterresults_filename="access_to_technology-student-_counter_results.tsv",
#             raw_counterresults_filename="raw-access_to_technology-student-counter_results.tsv"
#             )


# # Computer OS Counter
# wordlist = {"windows":0,"mac os":0,"linux":0,"Mac OS":0}
# BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
#             "studentlist.tsv",
#             15,
#             "Computer_OS Query - STUDENT -",
#             delimiterval="\t",
#             counterresults_filename="computeros-student-_results.tsv",
#             raw_counterresults_filename="raw-computeros-student-counter_results.tsv"
#             )



# # Frequency of Computer Usage Counter
# wordlist = {
# 		"almost everyday": 0,
# 		"everyday": 0,
# 		'occasionally': 0,
# 		'rarely': 0,
# 		'never': 0,
#  	}
# BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
#             "studentlist.tsv",
#             16,
#             "Frequency of Computer Usage - STUDENT - Query",
#             delimiterval="\t",
#             counterresults_filename="frequency_of_use_of_computers-student-_results.tsv",
#             raw_counterresults_filename="raw-frequency_of_use_of_computers-student-counter_results.tsv"
#               )

# # Do you own Smart Phones? Counter
# wordlist = {"yes":0,"no":0}
# BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
#             "studentlist.tsv",
#             17,
#             "Smart Phones Owner - STUDENT - Query",
#             delimiterval="\t",
#             counterresults_filename="OwnerofPhone-counter-student-_results.tsv",
#             raw_counterresults_filename="raw-OwnerofPhone-student--counter_results.tsv"
#               )

# # What operating system does your smart phone have?? Counter
# wordlist = {"android":0,
#  			"ios":0,
#  			"windows":0,
#  			"blackberry":0,
#  			"huawei":0,
# 		}

# BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
#             "studentlist.tsv",
#             18,
#             "OSPhoneCounter - STUDENT - Query",
#             delimiterval="\t",
#             counterresults_filename="OSPhone-student-counter_results.tsv",
#             raw_counterresults_filename="raw-OSPhoneCounter-student-counter_results.tsv"
#               )



# # In a weekly basis, how often do you use your smart phone?  Counter
# wordlist = {
# 		"almost everyday": 0,
# 		"everyday": 0,
# 		'occasionally': 0,
# 		'rarely': 0,
# 		'never': 0,
#  	}
# BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
#             "studentlist.tsv",
#             19,
#             "FrequencyofPhoneUsage - STUDENT - Query",
#             delimiterval="\t",
#             counterresults_filename="FrequencyofPhoneUsage-student-counter_results.tsv",
#             raw_counterresults_filename="raw-FrequencyofPhoneUsage-student--counter_results.tsv"
#               )


# # Do you have computer Tablets??  Counter
# wordlist = {"yes":0,"no":0}
# BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
#             "studentlist.tsv",
#             20,
#             "AccessToTablets - STUDENT - Query",
#             delimiterval="\t",
#             counterresults_filename="AccessToTablets-student-counter_results.tsv",
#             raw_counterresults_filename="raw-AccessToTablets-student-counter_results.tsv"
#               )


# # What operating system does your tablet have?   Counter
# wordlist = {"android": 0,
#  			"ios": 0,
#  			"windows": 0,
# 		}
# BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
#             "studentlist.tsv",
#             21,
#             "TabletOS - STUDENT - Query",
#             delimiterval="\t",
#             counterresults_filename="TabletOS-student-counter_results.tsv",
#             raw_counterresults_filename="raw-TabletOS-student-counter_results.tsv"
#               )

# # How often do you use your tablet? Counter
# wordlist = {"everyday":0,
#  			"almost everyday":0,
#  			"occasionally": 0,
#  			"rarely": 0,
#  			"never": 0,
# 		}

# BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
#             "studentlist.tsv",
#             22,
#             "FrequencyofTabletUsage - STUDENT - Query",
#             delimiterval="\t",
#             counterresults_filename="FrequencyofTabletUsage-student-counter_results.tsv",
#             raw_counterresults_filename="raw-FrequencyofTabletUsage-student-counter_results.tsv"
#               )

wordlist = {}
# Do you have Internet Services at home (ADSL Broadband, WIFI broadband, Pocket Wifi, Mobile Data etc)? 23 : Student
BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
            "studentlist.tsv",
            23,
            "AvailableInternetServices - STUDENT - Query",
            delimiterval="\t",
            counterresults_filename="AvailableInternetServices-student-counter_results.tsv",
            raw_counterresults_filename="raw-AvailableInternetServices-student-counter_results.tsv"
              )


wordlist = {}
# How do you connect to the Internet? (Please check all applicable answers)? 24 : Student
BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
            "studentlist.tsv",
            24,
            "MethodofConnectiontoTheInternet - STUDENT - Query",
            delimiterval="\t",
            counterresults_filename="MethodofConnectiontoTheInternet-student-counter_results.tsv",
            raw_counterresults_filename="raw-MethodofConnectiontoTheInternet-student-counter_results.tsv"
              )

wordlist = {}
# What type of internet subscription do you have? 25 : Student
BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
            "studentlist.tsv",
            25,
            "Internet_Subscription - STUDENT - Query",
            delimiterval="\t",
            counterresults_filename="Internet_Subscription-student-counter_results.tsv",
            raw_counterresults_filename="raw-Internet_Subscription-student-counter_results.tsv"
              )

wordlist = {}
# What/Who is your main Internet service provider? 26 :  Student
BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
            "studentlist.tsv",
            26,
            "Internet_Service_Provider - STUDENT - Query",
            delimiterval="\t",
            counterresults_filename="Internet_Service_Provider-student-counter_results.tsv",
            raw_counterresults_filename="raw-Internet_Service_Provider-student-counter_results.tsv"
              )


wordlist = {}
# How fast is your internet connectivity? 27 :  Student
BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
            "studentlist.tsv",
            27,
            "Internet_Speed - STUDENT - Query",
            delimiterval="\t",
            counterresults_filename="Internet_Speed-student-counter_results.tsv",
            raw_counterresults_filename="raw-Internet_Speed-student-counter_results.tsv"
			)