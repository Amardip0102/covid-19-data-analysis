########################################################################
# import dependencies
########################################################################
from support_func import read_data as rd
import pandas as pd
import numpy as np


########################################################################
# Calculate Number of days
#######################################################################
def calculate_num_days(df_date):
    df_days = pd.DataFrame(columns=['days'])
    df_days['days'] = pd.to_datetime('today') - pd.to_datetime(df_date)
    df_days['days'] = df_days['days']/np.timedelta64(1,'D')
    return df_days['days']
#########################################################################


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
        (df_travel_risk['Stll There'] == "No") & (df_travel_risk['When Came Back'] <= 14) &
        (df_travel_risk['When Came Back'] >= 0)& (df_travel_risk['Transportation'] == "Public Transport"),
        (df_travel_risk['Stll There'] == "No") & (df_travel_risk['When Came Back'] <= 14) &
        (df_travel_risk['When Came Back'] >= 0)&(df_travel_risk['Transportation'] == "Personal Vehicle"),
        (df_travel_risk['Stll There'] == "No") & (df_travel_risk['When Came Back'] > 14) &
        (df_travel_risk['Transportation'] == "Public Transport"),
        (df_travel_risk['Stll There'] == "No") & (df_travel_risk['When Came Back'] > 14) &
        (df_travel_risk['Transportation'] == "Personal Vehicle")
    ]

    outputs = ['High', 'High', 'Medium', 'Medium', 'Low']
    rd.df_adv_col_out['Travel Risk'] = np.select(conditions, outputs, default='Low')

    return 0
