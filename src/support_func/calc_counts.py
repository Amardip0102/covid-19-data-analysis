from support_func import read_data as rd
from support_func import filtering as filt
############################################################
# Debug Variables
############################################################
debug = False
############################################################

###########################################################


#############################################################
# FUNCTION : calculate designations counts based on teams
#
#############################################################
def calculate_designations_count(data_table):
    listD = []


    # Sequence to Append
    # 'All', 'Engineer', 'Sr. Engineer', 'Specialist', 'Sr.  Specialist', 'Tech-Team Lead', 'Dy. Manager', 'Manager',
    #                 'Assistant Manager', 'Sr. Manager', 'Dy. Architect', 'Architect', 'Sr. Architect',
    #                 'Dy. General Manager', 'General Manager', 'Other'
    if data_table.empty:
        listD = [None] * 15
    else:
        listD.append(len(data_table[data_table['Designation'] == 'Engineer']))
        listD.append(len(data_table[data_table['Designation'] == 'Sr. Engineer']))
        listD.append(len(data_table[data_table['Designation'] == 'Specialist']))
        listD.append(len(data_table[data_table['Designation'] == 'Sr. Specialist']))
        listD.append(len(data_table[data_table['Designation'] == 'Tech/Team Lead']))
        listD.append(len(data_table[data_table['Designation'] == 'Dy. Manager']))
        listD.append(len(data_table[data_table['Designation'] == 'Manager']))
        listD.append(len(data_table[data_table['Designation'] == 'Assistant Manager']))
        listD.append(len(data_table[data_table['Designation'] == 'Sr. Manager']))
        listD.append(len(data_table[data_table['Designation'] == 'Dy. Architect']))
        listD.append(len(data_table[data_table['Designation'] == 'Architect']))
        listD.append(len(data_table[data_table['Designation'] == 'Sr. Architect']))
        listD.append(len(data_table[data_table['Designation'] == 'Dy. General Manager']))
        listD.append(len(data_table[data_table['Designation'] == 'General Manager']))
        listD.append(len(data_table[data_table['Designation'] == 'Other']))

    return listD
############################################################


#############################################################
# FUNCTION : calculate Age counts based on teams
#
#############################################################
def calculate_age_counts(data_table):
    listA = []

    if data_table.empty:
        listA = [None] * 4
    else:
        listA.append(len(data_table[data_table['Age'] == filt.age['20-30 Years']]))
        listA.append(len(data_table[data_table['Age'] == filt.age['30-40 Years']]))
        listA.append(len(data_table[data_table['Age'] == filt.age['40-50 Years']]))
        listA.append(len(data_table[data_table['Age'] == filt.age['> 50 Years']]))
    return listA
#############################################################


#############################################################
# FUNCTION : calculate work experience counts based on teams
#
#############################################################
def calculate_gender_count(data_table):
    listG = []
    if data_table.empty:
        listG = [None] * 3
    else:
        listG.append(len(data_table[data_table['Gender'] == 'Male']))
        listG.append(len(data_table[data_table['Gender'] == 'Female']))
        listG.append(len(data_table[data_table['Gender'] == 'Other']))

    return listG
#############################################################
#############################################################
# FUNCTION : calculate Travel history counts based on teams
#
#############################################################

def calculate_Travel_count(data_table):
    listG = []

    if data_table.empty:
        listG = [None] * 3
    else:
        listG.append(len(data_table[data_table['Travel Risk'] == 'High']))
        listG.append(len(data_table[data_table['Travel Risk'] == 'Medium']))
        listG.append(len(data_table[data_table['Travel Risk'] == 'Low']))

    return listG


#############################################################
# FUNCTION : calculate work experience counts based on teams
#
#############################################################
def calcWorkExperience(data_table):

    listWE = []
    # ['Name', 'ID', 'Team', 'Experience', 'Designation', 'Age', 'Gender']

    if data_table.empty:
        listWE = [None] * 4
    else:
        listWE.append(len(data_table[data_table['Experience'] == filt.experience['0-2 Years']]))
        listWE.append(len(data_table[data_table['Experience'] == filt.experience['2-5 Years']]))
        listWE.append(len(data_table[data_table['Experience'] == filt.experience['5-10 Years']]))
        listWE.append(len(data_table[data_table['Experience'] == filt.experience['> 10 Years']]))
    # debug code
    if debug is True:
        print(listWE)
    return listWE
#############################################################


#############################################################
# FUNCTION : calculate wwork home distance counts based on teams
#
#############################################################
def calcWork_home_distance(data_table):
    listWE = []

    if data_table.empty:
        listWE = [None] * 5
    else:
        listWE.append(len(data_table[data_table['Distance'] == filt.distance['0-5 Kms']]))
        listWE.append(len(data_table[data_table['Distance'] == filt.distance['6-10 kms']]))
        listWE.append(len(data_table[data_table['Distance'] == filt.distance['10-15 Kms']]))
        listWE.append(len(data_table[data_table['Distance'] == filt.distance['15-20 Kms']]))
        listWE.append(len(data_table[data_table['Distance'] == filt.distance['>20 Kms']]))

    return listWE
#############################################################
#############################################################
# FUNCTION : calculate hotspot exposure counts based on teams
#
#############################################################
def calculate_hotspot_exposure_counts(data_table):
    listA = []

    if data_table.empty:
        listA = [None] * 3
    else:
        listA.append(len(data_table[data_table['RedZone Exposure Risk'] == 'High']))
        listA.append(len(data_table[data_table['RedZone Exposure Risk'] == 'Medium']))
        listA.append(len(data_table[data_table['RedZone Exposure Risk'] == 'Low']))

    return listA
#############################################################

#############################################################
# FUNCTION : calculate Covid19 exposure counts based on teams
#
#############################################################
def calculate_covid_exposure_counts(data_table):
    listA = []

    if data_table.empty:
        listA = [None] * 3
    else:
        listA.append(len(data_table[data_table['Covid Contact Risk'] == 'High']))
        listA.append(len(data_table[data_table['Covid Contact Risk'] == 'Medium']))
        listA.append(len(data_table[data_table['Covid Contact Risk'] == 'Low']))

    return listA
#############################################################


#############################################################
def calculate_staying_people_counts(data_table):
    listA = []

    if data_table.empty:
        listA = [None] * 3
    else:
        listA.append(len(data_table[data_table['Members'] == filt.personcount['0-5 persons']]))
        listA.append(len(data_table[data_table['Members'] == filt.personcount['5-10 persons']]))
        listA.append(len(data_table[data_table['Members'] == filt.personcount['> 10 persons']]))

    return listA
#############################################################


#############################################################
def calculate_health_risk_counts(data_table):
    listA = []

    if data_table.empty:
        listA = [None] * 3
    else:
        listA.append(len(data_table[data_table['Health Risk'] == 'High']))
        listA.append(len(data_table[data_table['Health Risk'] == 'Medium']))
        listA.append(len(data_table[data_table['Health Risk'] == 'Low']))

    return listA
#############################################################


##############################################################
#
##############################################################
def filter_advance_data(origdata, travel_risk, work_dist, living_with, kids_srcitizen,office_mode_transport,
                        redzone, covid_contact, health_risk, cache):

    # check if team name is not All
    if 'All' not in cache['Team']:
        if cache['Team']:
            origdata = origdata[(origdata['Team'].isin(cache['Team']))]

    # check if designation is not all and filtering is required
    if 'All' not in cache['Designation']:
        if cache['Designation']:
            origdata = origdata[(origdata['Designation'].isin(cache['Designation']))]

    # check if experience is not All
    if 'All' not in cache['Exp']:
        if cache['Exp']:
            origdata = origdata[(origdata['Experience'].isin(cache['Exp']))]

    # check if gender is not all
    if 'All' not in cache['Gender']:
        if cache['Gender']:
            origdata = origdata[(origdata['Gender'].isin(cache['Gender']))]

    # check if age is not All
    if 'All' not in cache['Age']:
        if cache['Age']:
            origdata = origdata[(origdata['Age'].isin(cache['Age']))]

    ###########################################################
    # Advance Filter: travel_risk, work_dist, living_with, redzone, covid_contact, health_risk,
    ###########################################################
    if 'All' not in travel_risk:
        if travel_risk:
            origdata = origdata[(origdata['Travel Risk'].isin(travel_risk))]

    # check if work_dist
    if 'All' not in work_dist:
        if work_dist:
            origdata = origdata[(origdata['Distance'].isin(work_dist))]

    # check if living_with
    if 'All' not in living_with:
        if living_with:
            origdata = origdata[(origdata['Members'].isin(living_with))]

    #check if senior citizen kids
    if kids_srcitizen != 'All':
        is_kids_srcitizen = origdata['SrCitizen_Kids'] == kids_srcitizen
        origdata = origdata[is_kids_srcitizen]

    # check if office mode of transport
    if 'All' not in office_mode_transport:
        if office_mode_transport:
            origdata = origdata[(origdata['Transport mode office'].isin(office_mode_transport))]

    # check if redZOne Exposed
    if 'All' not in redzone:
        if redzone:
            origdata = origdata[(origdata['RedZone Exposure Risk'].isin(redzone))]

    # check if covid contact
    if 'All' not in covid_contact:
        if covid_contact:
            origdata = origdata[(origdata['Covid Contact Risk'].isin(covid_contact))]

    if 'All' not in health_risk:
        if health_risk:
            origdata = origdata[(origdata['Health Risk'].isin(health_risk))]

    return origdata


def calculate_srcitizen_kids_counts(data_table):
    listS = []

    if data_table.empty:
        listS = [None] * 2
    else:
        listS.append(len(data_table[data_table['SrCitizen_Kids'] == 'Yes']))
        listS.append(len(data_table[data_table['SrCitizen_Kids'] == 'No']))

    return listS


def calculate_mode_transport_counts(data_table):
    listT = []

    if data_table.empty:
        listT = [None] * 5
    else:
        listT.append(len(data_table[data_table['Transport mode office'] == '2 Wheeler']))
        listT.append(len(data_table[data_table['Transport mode office'] == '4 Wheeler']))
        listT.append(len(data_table[data_table['Transport mode office'] == 'Shared Car']))
        listT.append(len(data_table[data_table['Transport mode office'] == 'Public Transport']))
        listT.append(len(data_table[data_table['Transport mode office'] == 'By Walk']))

    return listT
