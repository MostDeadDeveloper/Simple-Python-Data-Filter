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

wordlist = {}
BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
            "facultylist.tsv",
            11,
            "Employment Status - Faculty Query",
            delimiterval="\t",
            counterresults_filename="employment_status-faculty-counter_results.tsv",
            raw_counterresults_filename="raw-employment_status-faculty-counter_results.tsv"
            )

wordlist = {}
BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
            "facultylist.tsv",
            13,
            "Age_Group - Faculty Query",
            delimiterval="\t",
            counterresults_filename="Age_Group-faculty-counter_results.tsv",
            raw_counterresults_filename="raw-Age_Group-faculty-counter_results.tsv"
            )

wordlist = {}
BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
            "facultylist.tsv",
            14,
            "AccessToComputers - Faculty Query",
            delimiterval="\t",
            counterresults_filename="AccessToComputers-faculty-counter_results.tsv",
            raw_counterresults_filename="raw-AccessToComputers-faculty-counter_results.tsv"
            )

wordlist = {}
BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
            "facultylist.tsv",
            15,
            "computeroperatingsystem - Faculty Query",
            delimiterval="\t",
            counterresults_filename="computeroperatingsystem-faculty-counter_results.tsv",
            raw_counterresults_filename="raw-computeroperatingsystem-faculty-counter_results.tsv"
            )

wordlist = {
		"almost everyday": 0,
		"everyday": 0,
		'occasionally': 0,
		'rarely': 0,
		'never': 0,
 	}
BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
            "facultylist.tsv",
            16,
            "FrequencyofUseinComputers - Faculty Query",
            delimiterval="\t",
            counterresults_filename="FrequencyofUseinComputers-faculty-counter_results.tsv",
            raw_counterresults_filename="raw-FrequencyofUseinComputers-faculty-counter_results.tsv"
            )


wordlist = {}
BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
            "facultylist.tsv",
            17,
            "AccessToPhones - Faculty Query",
            delimiterval="\t",
            counterresults_filename="AccessToPhones-faculty-counter_results.tsv",
            raw_counterresults_filename="raw-AccessToPhones-faculty-counter_results.tsv"
            )

wordlist = {}
BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
            "facultylist.tsv",
            18,
            "PhoneOS - Faculty Query",
            delimiterval="\t",
            counterresults_filename="PhoneOS-faculty-counter_results.tsv",
            raw_counterresults_filename="raw-PhoneOS-faculty-counter_results.tsv"
            )

wordlist = {
		"almost everyday": 0,
		"everyday": 0,
		'occasionally': 0,
		'rarely': 0,
		'never': 0,
 	}
BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
            "facultylist.tsv",
            19,
            "FrequencyofPhoneUsage - Faculty Query",
            delimiterval="\t",
            counterresults_filename="FrequencyofPhoneUsage-faculty-counter_results.tsv",
            raw_counterresults_filename="raw-FrequencyofPhoneUsage-faculty-counter_results.tsv"
            )

wordlist = {}
BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
            "facultylist.tsv",
            20,
            "AccessToTablets - Faculty Query",
            delimiterval="\t",
            counterresults_filename="AccessToTablets-faculty-counter_results.tsv",
            raw_counterresults_filename="raw-AccessToTablets-faculty-counter_results.tsv"
            )


wordlist = {}
BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
            "facultylist.tsv",
            21,
            "TabletOS - Faculty Query",
            delimiterval="\t",
            counterresults_filename="TabletOS-faculty-counter_results.tsv",
            raw_counterresults_filename="raw-TabletOS-faculty-counter_results.tsv"
            )

wordlist = {
		"almost everyday": 0,
		"everyday": 0,
		'occasionally': 0,
		'rarely': 0,
		'never': 0,
 	}
BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
            "facultylist.tsv",
            22,
            "FrequencyofTabletUsage - Faculty Query",
            delimiterval="\t",
            counterresults_filename="FrequencyofTabletUsage-faculty-counter_results.tsv",
            raw_counterresults_filename="raw-FrequencyofTabletUsage-faculty-counter_results.tsv"
            )

wordlist = {}
BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
            "facultylist.tsv",
            23,
            "AccessToInternetServices - Faculty Query",
            delimiterval="\t",
            counterresults_filename="AccessToInternetServices-faculty-counter_results.tsv",
            raw_counterresults_filename="raw-AccessToInternetServices-faculty-counter_results.tsv"
            )

# wordlist = {}
# BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
#             "facultylist.tsv",
#             24,
#             "AccessToInternetServices - Faculty Query",
#             delimiterval="\t",
#             counterresults_filename="AccessToInternetServices-faculty-counter_results.tsv",
#             raw_counterresults_filename="raw-AccessToInternetServices-faculty-counter_results.tsv"
#             )

wordlist = {}
BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
            "facultylist.tsv",
            25,
            "TypeofInternetSubscription - Faculty Query",
            delimiterval="\t",
            counterresults_filename="TypeofInternetSubscription-faculty-counter_results.tsv",
            raw_counterresults_filename="raw-TypeofInternetSubscription-faculty-counter_results.tsv"
            )

wordlist = {}
BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
            "facultylist.tsv",
            26,
            "MainInternetServiceProvider - Faculty Query",
            delimiterval="\t",
            counterresults_filename="MainInternetServiceProvider-faculty-counter_results.tsv",
            raw_counterresults_filename="raw-MainInternetServiceProvider-faculty-counter_results.tsv"
            )

wordlist = {}
BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
            "facultylist.tsv",
            27,
            "InternetConnectivitySpeed - Faculty Query",
            delimiterval="\t",
            counterresults_filename="InternetConnectivitySpeed-faculty-counter_results.tsv",
            raw_counterresults_filename="raw-InternetConnectivitySpeed-faculty-counter_results.tsv"
            )

wordlist = {}
BaseCounter_self_aware_dictionary_and_output_Numerical_Data(wordlist,
            "facultylist.tsv",
            28,
            "InternetConnectivityCost - Faculty Query",
            delimiterval="\t",
            counterresults_filename="InternetConnectivityCost-faculty-counter_results.tsv",
            raw_counterresults_filename="raw-InternetConnectivityCost-faculty-counter_results.tsv"
            )

