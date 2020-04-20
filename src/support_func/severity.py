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

    :return:
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
