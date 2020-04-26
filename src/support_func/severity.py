########################################################################
# import dependencies
########################################################################
from support_func import read_data as rd
import pandas as pd
import numpy as np

#######################################################################
# Constant Section : which shall be later replaced by dynamic values
######################################################################
const_num_days = 14


########################################################################
# Calculate Number of days
#######################################################################
def calculate_num_days(df_date):
    df_days = pd.DataFrame(columns=['days'])
    df_days['days'] = pd.to_datetime('today') - pd.to_datetime(df_date)
    df_days['days'] = df_days['days'] / np.timedelta64(1, 'D')
    return df_days['days']


#########################################################################


########################################################################
#
########################################################################


def eval_affected_areas_exposure_severity():
    '''
    |-------------------------------------------------------------------------------|
    | VISITED HOT SPOT AREAS |  | VISITED HEALTH CARE    | OUTPUT     |
    |-------------------------------------------------------------------------------|
    |       YES	             |            YES	         |   HIGH     |
    |       YES              |            NO             |   MEDIUM   |
    |       NO               |            YES            |   MEDIUM   |
    |       NO               |            NO             |   LOW      |
    |-------------------------------------------------------------------------------|


    '''

    df_intermediate = rd.df_adv_col_in.copy()
    df_intermediate['Redzone_visit'] = df_intermediate['Redzone_visit'].replace(np.nan, 'No')
    df_intermediate['Healthcare_visit'] = df_intermediate['Healthcare_visit'].replace(np.nan, 'No')

    conditions = [
        ((df_intermediate['Redzone_visit'] == 'No') & (df_intermediate['Healthcare_visit'] == 'No')),
        ((df_intermediate['Redzone_visit'] == 'Yes') & (df_intermediate['Healthcare_visit'] == 'No')),
        ((df_intermediate['Redzone_visit'] == 'No') & (df_intermediate['Healthcare_visit'] == 'Yes')),
        ((df_intermediate['Redzone_visit'] == 'Yes') & (df_intermediate['Healthcare_visit'] == 'Yes'))

    ]
    output = ['Low', 'Medium', 'Medium', 'High']

    for k in range(len(output)):
        rd.df_adv_col_out.loc[conditions[k], 'RedZone Exposure Risk'] = output[k]

    return 0


def eval_contact_covid_severity():
    '''
    --------------------------------------------------------------------------------------------------------
    contact with covid19 patient | contact with travel history	 | allowed to work from family |	severity
    --------------------------------------------------------------------------------------------------------
            YES	                            X	                            X	                    High
            No	                            Yes                         	Yes                    	 High
            No	                            Yes                         	No	                    Medium
            No	                            No	                           Yes	                    Medium
            No	                            No	                            No	                    Low
    --------------------------------------------------------------------------------------------------------
    :return: ['High', 'Medium', 'Low']
    '''
    # todo: Add Healthcare facility visited column here..
    # creating a local copy
    df_contact_covid = rd.df_adv_col_in[['Contact_Travel', 'Living_with_Govt_HealthCare', 'Contact_Covid']].copy()

    # decision table:

    conditions = [
        (df_contact_covid['Contact_Covid'] == 'Yes'),
        (df_contact_covid['Contact_Travel'] == 'Yes') & (df_contact_covid['Living_with_Govt_HealthCare'] == 'Yes'),
        (df_contact_covid['Contact_Travel'] == 'Yes') & (df_contact_covid['Living_with_Govt_HealthCare'] == 'No'),
        (df_contact_covid['Contact_Travel'] == 'No') & (df_contact_covid['Living_with_Govt_HealthCare'] == 'Yes'),
        (df_contact_covid['Contact_Travel'] == 'No') & (df_contact_covid['Living_with_Govt_HealthCare'] == 'No')
    ]

    outputs = ['High', 'High', 'Medium', 'Medium', 'Low']

    rd.df_adv_col_out['Covid Contact Risk'] = np.select(conditions, outputs, default='Low')
    return 0


def eval_health_risk_severity():
    '''
    ---------------------------------------------------------------------------------------------------------------------
   	symptoms | Pre-Existing Health Condition |	tested for COVID-19	 | Result of your test | Recovered	|       Risk
	---------------------------------------------------------------------------------------------------------------------
     NO	            	NO	                            NO	                    X	                X	        LOW
	 NO	            	NO	                            YES	                    NEGATIVE	        X	        LOW
	 NO					NO								YES						POSITIVE			YES			MEDIUM
	 NO					NO								YES						POSITIVE			NO			HIGH
	 NO					YES 							NO						X					X			LOW
	 NO					YES 							YES						NEGATIVE			X			LOW
	 NO					YES 							YES						POSITIVE			YES			HIGH
	 NO					YES 							YES						POSITIVE			NO			HIGH
	 YES				NO								NO						X					X			HIGH
	 YES				NO								YES						NEGATIVE			X			MEDIUM
	 YES				NO								YES						POSITIVE			YES			HIGH
	 YES				NO								YES						POSITIVE			NO			HIGH
	 YES			    YES 							NO						X					X			MEDIUM
	 YES				YES 							YES						NEGATIVE			X			MEDIUM
	 YES				YES 							YES						POSITIVE			YES			HIGH
	 YES				YES 							YES						POSITIVE			NO			HIGH

    '''
    df_health_risk = rd.df_adv_col_in[['Symptoms', 'Pre_Existing_Disease', 'Tested_For_COVID',
                                       'Result_Of_Test', 'Recovered']].copy()

    df_health_risk['Pre_Existing_Disease'] = df_health_risk['Pre_Existing_Disease'].replace(np.nan, 'No')

    df_health_risk['Pre_Existing_Disease'] = np.where(df_health_risk['Pre_Existing_Disease'] == 'None of the above', 'No',
                                                      df_health_risk['Pre_Existing_Disease'])

    df_health_risk['Pre_Existing_Disease'] = np.where(df_health_risk['Pre_Existing_Disease'] == '','No',
                                                      df_health_risk['Pre_Existing_Disease'])


    conditions = [  # Low
        (df_health_risk["Symptoms"] == "None of the above") & (
                df_health_risk["Pre_Existing_Disease"] == "No") & (
                df_health_risk["Tested_For_COVID"] == "No"),
        (df_health_risk["Symptoms"] == "None of the above") & (
                df_health_risk["Pre_Existing_Disease"] != "No") & (
                df_health_risk["Tested_For_COVID"] == "No"),
        (df_health_risk["Symptoms"] == "None of the above") & (
                df_health_risk["Pre_Existing_Disease"] == "No") & (
                df_health_risk["Tested_For_COVID"] == "Yes") & (
                df_health_risk["Result_Of_Test"] == "Negative"),
        (df_health_risk["Symptoms"] == "None of the above") & (
                df_health_risk["Pre_Existing_Disease"] != "No")  & (
                df_health_risk["Tested_For_COVID"] == "Yes") & (
                df_health_risk["Result_Of_Test"] == "Negative"),

        # Medium
        (df_health_risk["Symptoms"] == "None of the above") & (
                df_health_risk["Pre_Existing_Disease"] == "No") & (
                df_health_risk["Tested_For_COVID"] == "Yes") & (
                df_health_risk["Result_Of_Test"] == "Positive") & (
                df_health_risk["Recovered"] == "Yes"),

        (df_health_risk["Symptoms"] != "None of the above") & (
                df_health_risk["Pre_Existing_Disease"] == "No") & (
                df_health_risk["Tested_For_COVID"] == "Yes") & (
                df_health_risk["Result_Of_Test"] == "Negative"),

        (df_health_risk["Symptoms"] != "None of the above") & (
                df_health_risk["Pre_Existing_Disease"] != "No") & (
                df_health_risk["Tested_For_COVID"] == "No"),

        (df_health_risk["Symptoms"] != "None of the above") & (
                df_health_risk["Pre_Existing_Disease"] != "No") & (
                df_health_risk["Tested_For_COVID"] == "Yes") & (
                df_health_risk["Result_Of_Test"] == "Negative"),

        # High
        (df_health_risk["Symptoms"] == "None of the above") & (
                df_health_risk["Pre_Existing_Disease"] == "No")  & (
                df_health_risk["Tested_For_COVID"] == "Yes") & (
                df_health_risk["Result_Of_Test"] == "Positive") & (
                df_health_risk["Recovered"] == "No"),

        (df_health_risk["Symptoms"] == "None of the above") & (
                df_health_risk["Pre_Existing_Disease"] != "No") & (
                df_health_risk["Tested_For_COVID"] == "Yes") & (
                df_health_risk["Result_Of_Test"] == "Positive") & (
                df_health_risk["Recovered"] == "Yes"),

        (df_health_risk["Symptoms"] == "None of the above") & (
                df_health_risk["Pre_Existing_Disease"] != "No") & (
                df_health_risk["Tested_For_COVID"] == "Yes") & (
                df_health_risk["Result_Of_Test"] == "Positive") & (
                df_health_risk["Recovered"] == "No"),

        (df_health_risk["Symptoms"] != "None of the above") & (
                df_health_risk["Pre_Existing_Disease"] == "No") & (
                df_health_risk["Tested_For_COVID"] == "No"),

        (df_health_risk["Symptoms"] != "None of the above") & (
                df_health_risk["Pre_Existing_Disease"] == "No") & (
                df_health_risk["Tested_For_COVID"] == "Yes") & (
                df_health_risk["Result_Of_Test"] == "Positive") & (
                df_health_risk["Recovered"] == "Yes"),

        (df_health_risk["Symptoms"] != "None of the above") & (
                df_health_risk["Pre_Existing_Disease"] == "No") & (
                df_health_risk["Tested_For_COVID"] == "Yes") & (
                df_health_risk["Result_Of_Test"] == "Positive") & (
                df_health_risk["Recovered"] == "No"),

        (df_health_risk["Symptoms"] != "None of the above") & (
                df_health_risk["Pre_Existing_Disease"] != "No") & (
                df_health_risk["Tested_For_COVID"] == "Yes") & (
                df_health_risk["Result_Of_Test"] == "Positive") & (
                df_health_risk["Recovered"] == "Yes"),

        (df_health_risk["Symptoms"] != "None of the above") & (
                df_health_risk["Pre_Existing_Disease"] != "No") & (
                df_health_risk["Tested_For_COVID"] == "Yes") & (
                df_health_risk["Result_Of_Test"] == "Positive") & (
                df_health_risk["Recovered"] == "No"),

    ]
    outputs = ['Low', 'Low', 'Low', 'Low', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'High', 'High', 'High',
               'High', 'High', 'High', 'High']

    rd.df_adv_col_out['Health Risk'] = np.select(conditions, outputs)

    return 0


def eval_travel_risk_severity():
    '''
    Travel Risk
    ------------------------------------------------------------------------------
    Travelled   |  Still there	|   when came            |  Transport	 |  Output
        Yes	    |       Yes	    |   X	                 |  X	        High
        Yes	    |       No	    |   Less than 14 days	 |  Public	    High
        Yes	    |       No	    |   Less than 14 days	 |  Private	    Medium
        Yes     |   	No	    |   More than 14 days	 |  Public	    Medium
        Yes	    |       No	    |   More than 14 days	 |  Private	    Low
        No	    |       X	    |   X	                 |  X	        Low
    ---------------------------------------------------------------------------------

    :return:
    '''
    # copy data locally
    df_travel_risk = rd.df_adv_col_in[['Travel out Pune', 'Stll There', 'When Came Back', 'Transportation']].copy()

    # convert date to days and replace the column
    df_travel_risk['When Came Back'] = calculate_num_days(rd.df_adv_col_in['When Came Back'])

    # replace -ve values with zero
    # df_travel_risk['When Came Back'] = np.where(df_travel_risk['When Came Back'] < 0 ,
    # 0, df_travel_risk['When Came Back'])

    # Replace all public way of transports with "Public Transport".

    df_travel_risk['Transportation'] = np.where(df_travel_risk['Transportation'] == 'Flight', 'Public Transport',
                                                df_travel_risk['Transportation'])

    df_travel_risk['Transportation'] = np.where(df_travel_risk['Transportation'] == 'Bus', 'Public Transport',
                                                df_travel_risk['Transportation'])

    df_travel_risk['Transportation'] = np.where(df_travel_risk['Transportation'] == 'Train', 'Public Transport',
                                                df_travel_risk['Transportation'])

    # decision table:
    conditions = [
        (df_travel_risk['Travel out Pune'] == 'Yes') & (df_travel_risk['Stll There'] == "Yes"),
        (df_travel_risk['Stll There'] == "No") & (df_travel_risk['When Came Back'] <= const_num_days) &
        (df_travel_risk['When Came Back'] >= 0) & (df_travel_risk['Transportation'] == "Public Transport"),
        (df_travel_risk['Stll There'] == "No") & (df_travel_risk['When Came Back'] <= const_num_days) &
        (df_travel_risk['When Came Back'] >= 0) & (df_travel_risk['Transportation'] == "Personal Vehicle"),
        (df_travel_risk['Stll There'] == "No") & (df_travel_risk['When Came Back'] > const_num_days) &
        (df_travel_risk['Transportation'] == "Public Transport"),
        (df_travel_risk['Stll There'] == "No") & (df_travel_risk['When Came Back'] > const_num_days) &
        (df_travel_risk['Transportation'] == "Personal Vehicle")
    ]

    outputs = ['High', 'High', 'Medium', 'Medium', 'Low']
    rd.df_adv_col_out['Travel Risk'] = np.select(conditions, outputs, default='Low')

    return 0
