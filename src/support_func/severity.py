########################################################################
#
########################################################################


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
