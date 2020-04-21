########################################################################
#
########################################################################
import dash_html_components as html
from src.support_func import read_data as rd
import numpy as np
def eval_exposure_affected_severity():
    '''
    |-------------------------------------------------------------------------------|
    | STAY AT HOT SPOTS | VISITED HOT SPOT AREAS | VISITED HEALTH CARE | OUTPUT     |
    |-------------------------------------------------------------------------------|
    |       YES	        |           X 	          |         X	         |   HIGH
    |       NO                     YES                     X               MEDIUM   |
    |       NO                      NO                     YES             MEDIUM   |
    |       NO         |            NO           |         NO           |   LOW     |
    |-------------------------------------------------------------------------------|
    '''

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


    return 0


def eval_health_risk_severity():
    '''
      -Symptoms
      -pre-existing
      -TESTED for covid19
      -if positive
      -recovered
    :return: list = ['Low' , 'Medium' , 'High']
    Low -> Healthy
    Medium -> Moderate Healthy and tending towards unhealthy
    High -> Unhealthy
    '''
    df_health_risk = rd.df_adv_col_in[['Symptoms','Pre_Existing_Disease','Tested_For_COVID',
                         'Result_Of_Test','Recovered']].copy()

    print(df_health_risk.Symptoms)
    len_of_index = len(df_health_risk.Symptoms)
    Conditions = [ #Low
                   (df_health_risk["Symptoms"] == "None of the above") & (
                           df_health_risk["Pre_Existing_Disease"] == "None of the above") & (
                           df_health_risk["Tested_For_COVID"] == "No"),
                   (df_health_risk["Symptoms"] == "None of the above") & (
                           df_health_risk["Pre_Existing_Disease"] != "None of the above") & (
                           df_health_risk["Tested_For_COVID"] == "No"),
                   (df_health_risk["Symptoms"] == "None of the above") & (
                           df_health_risk["Pre_Existing_Disease"] == "None of the above") & (
                           df_health_risk["Tested_For_COVID"] == "Yes") & (
                           df_health_risk["Result_Of_Test"] == "Negative"),
                   (df_health_risk["Symptoms"] == "None of the above") & (
                           df_health_risk["Pre_Existing_Disease"] != "None of the above") & (
                           df_health_risk["Tested_For_COVID"] == "Yes") & (
                           df_health_risk["Result_Of_Test"] == "Negative"),

                    #Medium
                   (df_health_risk["Symptoms"] == "None of the above") & (
                           df_health_risk["Pre_Existing_Disease"] == "None of the above") & (
                           df_health_risk["Tested_For_COVID"] == "Yes") & (
                           df_health_risk["Result_Of_Test"] == "Positive") & (
                           df_health_risk["Recovered"] == "Yes"),

                   (df_health_risk["Symptoms"] != "None of the above") & (
                           df_health_risk["Pre_Existing_Disease"] == "None of the above") & (
                           df_health_risk["Tested_For_COVID"] == "Yes") & (
                           df_health_risk["Result_Of_Test"] == "Negative"),

                   (df_health_risk["Symptoms"] != "None of the above") & (
                           df_health_risk["Pre_Existing_Disease"] != "None of the above") & (
                           df_health_risk["Tested_For_COVID"] == "No"),

                   (df_health_risk["Symptoms"] != "None of the above") & (
                           df_health_risk["Pre_Existing_Disease"] != "None of the above") & (
                           df_health_risk["Tested_For_COVID"] == "Yes") & (
                           df_health_risk["Result_Of_Test"] == "Negative"),


                   #High
                   (df_health_risk["Symptoms"] == "None of the above") & (
                           df_health_risk["Pre_Existing_Disease"] == "None of the above") & (
                           df_health_risk["Tested_For_COVID"] == "Yes") & (
                           df_health_risk["Result_Of_Test"] == "Positive") & (
                           df_health_risk["Recovered"] == "No"),

                   (df_health_risk["Symptoms"] == "None of the above") & (
                           df_health_risk["Pre_Existing_Disease"] != "None of the above") & (
                           df_health_risk["Tested_For_COVID"] == "Yes") & (
                           df_health_risk["Result_Of_Test"] == "Positive") & (
                           df_health_risk["Recovered"] == "Yes"),


                   (df_health_risk["Symptoms"] == "None of the above") & (
                           df_health_risk["Pre_Existing_Disease"] != "None of the above") & (
                           df_health_risk["Tested_For_COVID"] == "Yes") & (
                           df_health_risk["Result_Of_Test"] == "Positive")& (
                           df_health_risk["Recovered"] == "No"),

                   (df_health_risk["Symptoms"] != "None of the above") & (
                           df_health_risk["Pre_Existing_Disease"] == "None of the above") & (
                           df_health_risk["Tested_For_COVID"] == "No"),

                   (df_health_risk["Symptoms"] != "None of the above") & (
                           df_health_risk["Pre_Existing_Disease"] == "None of the above") & (
                           df_health_risk["Tested_For_COVID"] == "Yes") & (
                           df_health_risk["Result_Of_Test"] == "Positive") & (
                           df_health_risk["Recovered"] == "Yes"),

                   (df_health_risk["Symptoms"] != "None of the above") & (
                           df_health_risk["Pre_Existing_Disease"] == "None of the above") & (
                           df_health_risk["Tested_For_COVID"] == "Yes") & (
                           df_health_risk["Result_Of_Test"] == "Positive") & (
                           df_health_risk["Recovered"] == "No"),

                   (df_health_risk["Symptoms"] != "None of the above") & (
                           df_health_risk["Pre_Existing_Disease"] != "None of the above") & (
                           df_health_risk["Tested_For_COVID"] == "Yes") & (
                           df_health_risk["Result_Of_Test"] == "Positive") & (
                           df_health_risk["Recovered"] == "Yes"),

                   (df_health_risk["Symptoms"] != "None of the above") & (
                           df_health_risk["Pre_Existing_Disease"] != "None of the above") & (
                           df_health_risk["Tested_For_COVID"] == "Yes") & (
                           df_health_risk["Result_Of_Test"] == "Positive") & (
                           df_health_risk["Recovered"] == "No"),

                ]
    Outputs = ['Low','Low','Low','Low','Medium','Medium','Medium','Medium','High','High','High','High',
               'High','High','High','High']

    rd.df_adv_col_out['Health Risk']  = np.select(Conditions,Outputs)

    return 0


def eval_travel_risk_severity():
    '''
    Travel Risk
    ------------------------------------------------------------------------------
    Travelled   |  Still there	| Came Back |   when	        |   Transport	 |  Output
        Yes	            Yes	        X	        X	                    X	        High
        Yes	            No	        Yes	       Less than 14 days	    Public	    High
        Yes	            No	        Yes	        Less than 14 days	    Private	    Medium
        Yes         	No	        Yes	        More than 14 days	    Public	    Medium
        Yes	            No	        Yes	        More than 14 days	    Private	    Low
        No	            X	        X	        X	                    X	        Low
    ---------------------------------------------------------------------------------

    :return:
    '''
