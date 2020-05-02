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
def calculate_designations_count(team):
    listD = []
    if debug is True:
        print(team)
    df_designation = rd.df_sel_col.copy()
    # check if team name is not All
    if 'All' not in team:
        if team:
            df_designation = df_designation[(df_designation['Team'].isin(team))]

    # Sequence to Append
    # 'All', 'Engineer', 'Sr. Engineer', 'Specialist', 'Sr.  Specialist', 'Tech-Team Lead', 'Dy. Manager', 'Manager',
    #                 'Assistant Manager', 'Sr. Manager', 'Dy. Architect', 'Architect', 'Sr. Architect',
    #                 'Dy. General Manager', 'General Manager', 'Other'
    listD.append(len(df_designation[df_designation['Designation'] == 'Engineer']))
    listD.append(len(df_designation[df_designation['Designation'] == 'Sr. Engineer']))
    listD.append(len(df_designation[df_designation['Designation'] == 'Specialist']))
    listD.append(len(df_designation[df_designation['Designation'] == 'Sr. Specialist']))
    listD.append(len(df_designation[df_designation['Designation'] == 'Tech/Team Lead']))
    listD.append(len(df_designation[df_designation['Designation'] == 'Dy. Manager']))
    listD.append(len(df_designation[df_designation['Designation'] == 'Manager']))
    listD.append(len(df_designation[df_designation['Designation'] == 'Assistant Manager']))
    listD.append(len(df_designation[df_designation['Designation'] == 'Sr. Manager']))
    listD.append(len(df_designation[df_designation['Designation'] == 'Dy. Architect']))
    listD.append(len(df_designation[df_designation['Designation'] == 'Architect']))
    listD.append(len(df_designation[df_designation['Designation'] == 'Sr. Architect']))
    listD.append(len(df_designation[df_designation['Designation'] == 'Dy. General Manager']))
    listD.append(len(df_designation[df_designation['Designation'] == 'General Manager']))
    listD.append(len(df_designation[df_designation['Designation'] == 'Other']))
    return listD
############################################################


#############################################################
# FUNCTION : calculate Age counts based on teams
#
#############################################################
def calculate_age_counts(team):
    listA = []
    if debug is True:
        print(team)

    df_age = rd.df_sel_col.copy()

    if 'All' not in team:
        if team:
            df_age = df_age[(df_age['Team'].isin(team))]

    listA.append(len(df_age[df_age['Age'] == filt.age['20-30 Years']]))
    listA.append(len(df_age[df_age['Age'] == filt.age['30-40 Years']]))
    listA.append(len(df_age[df_age['Age'] == filt.age['40-50 Years']]))
    listA.append(len(df_age[df_age['Age'] == filt.age['> 50 Years']]))
    # debug code
    if debug is True:
        print(listA)
    return listA
#############################################################


#############################################################
# FUNCTION : calculate work experience counts based on teams
#
#############################################################
def calculate_gender_count(team):
    listG = []
    if debug is True:
        print(team)

    df_gender = rd.df_sel_col.copy()
    if 'All' not in team:
        if team:
            df_gender = df_gender[(df_gender['Team'].isin(team))]

    listG.append(len(df_gender[df_gender['Gender'] == 'Male']))
    listG.append(len(df_gender[df_gender['Gender'] == 'Female']))
    listG.append(len(df_gender[df_gender['Gender'] == 'Other']))
     # debug code
    if debug is True:
        print(listG)
    return listG
#############################################################
#############################################################
# FUNCTION : calculate Travel history counts based on teams
#
#############################################################

def calculate_Travel_count(team):
    listG = []
    if debug is True:
        print(team)

    df_travel = rd.df_adv_col_out.copy()

    if 'All' not in team:
        if team:
            df_travel = df_travel[(df_travel['Team'].isin(team))]

    listG.append(len(df_travel[df_travel['Travel Risk'] == 'High']))
    listG.append(len(df_travel[df_travel['Travel Risk'] == 'Medium']))
    listG.append(len(df_travel[df_travel['Travel Risk'] == 'Low']))
     # debug code
    if debug is True:
        print(listG)
    return listG


#############################################################
# FUNCTION : calculate work experience counts based on teams
#
#############################################################
def calcWorkExperience(team):
    if debug is True:
        print(team)
    listWE = []
    # ['Name', 'ID', 'Team', 'Experience', 'Designation', 'Age', 'Gender']
    df_work = rd.df_sel_col.copy()

    if 'All' not in team:
        if team:
            df_work = df_work[(df_work['Team'].isin(team))]

    listWE.append(len(df_work[df_work['Experience'] == filt.experience['0-2 Years']]))
    listWE.append(len(df_work[df_work['Experience'] == filt.experience['2-5 Years']]))
    listWE.append(len(df_work[df_work['Experience'] == filt.experience['5-10 Years']]))
    listWE.append(len(df_work[df_work['Experience'] == filt.experience['> 10 Years']]))

    # debug code
    if debug is True:
        print(listWE)
    return listWE
#############################################################


#############################################################
# FUNCTION : calculate wwork home distance counts based on teams
#
#############################################################
def calcWork_home_distance(team):
    if debug is True:
        print(team)
    listWE = []
    # ['Name', 'ID', 'Team', 'Experience', 'Designation', 'Age', 'Gender']
    df_work = rd.df_adv_col_out.copy()

    if 'All' not in team:
        if team:
            df_work = df_work[(df_work['Team'].isin(team))]

    listWE.append(len(df_work[df_work['Distance'] == filt.distance['0-5 Kms']]))
    listWE.append(len(df_work[df_work['Distance'] == filt.distance['6-10 kms']]))
    listWE.append(len(df_work[df_work['Distance'] == filt.distance['10-15 Kms']]))
    listWE.append(len(df_work[df_work['Distance'] == filt.distance['15-20 Kms']]))
    listWE.append(len(df_work[df_work['Distance'] == filt.distance['>20 Kms']]))

    # debug code
    if debug is True:
        print(listWE)
    return listWE
#############################################################
#############################################################
# FUNCTION : calculate hotspot exposure counts based on teams
#
#############################################################
def calculate_hotspot_exposure_counts(team):
    listA = []
    if debug is True:
        print(team)

    df_rzone = rd.df_adv_col_out.copy()
    if 'All' not in team:
        if team:
            df_rzone = df_rzone[(df_rzone['Team'].isin(team))]

    listA.append(len(df_rzone[df_rzone['RedZone Exposure Risk'] == 'High']))
    listA.append(len(df_rzone[df_rzone['RedZone Exposure Risk'] == 'Medium']))
    listA.append(len(df_rzone[df_rzone['RedZone Exposure Risk'] == 'Low']))
    # debug code
    if debug is True:
        print(listA)
    return listA
#############################################################

#############################################################
# FUNCTION : calculate Covid19 exposure counts based on teams
#
#############################################################
def calculate_covid_exposure_counts(team):
    listA = []
    if debug is True:
        print(team)

    df_cvd= rd.df_adv_col_out.copy()
    if 'All' not in team:
        if team:
            df_cvd = df_cvd[(df_cvd['Team'].isin(team))]

    listA.append(len(df_cvd[df_cvd['Covid Contact Risk'] == 'High']))
    listA.append(len(df_cvd[df_cvd['Covid Contact Risk'] == 'Medium']))
    listA.append(len(df_cvd[df_cvd['Covid Contact Risk'] == 'Low']))
    # debug code
    if debug is True:
        print(listA)
    return listA
#############################################################


#############################################################
def calculate_staying_people_counts(team):
    listA = []
    if debug is True:
        print(team)

    df_mem= rd.df_adv_col_out.copy()
    if 'All' not in team:
        if team:
            df_mem = df_mem[(df_mem['Team'].isin(team))]

    listA.append(len(df_mem[df_mem['Members'] == filt.personcount['0-5 persons']]))
    listA.append(len(df_mem[df_mem['Members'] == filt.personcount['5-10 persons']]))
    listA.append(len(df_mem[df_mem['Members'] == filt.personcount['> 10 persons']]))
    # debug code
    if debug is True:
        print(listA)
    return listA
#############################################################


#############################################################
def calculate_health_risk_counts(team):
    listA = []
    if debug is True:
        print(team)

    df_heal= rd.df_adv_col_out.copy()
    if 'All' not in team:
        if team:
            df_heal = df_heal[(df_heal['Team'].isin(team))]

    listA.append(len(df_heal[df_heal['Health Risk'] == 'High']))
    listA.append(len(df_heal[df_heal['Health Risk'] == 'Medium']))
    listA.append(len(df_heal[df_heal['Health Risk'] == 'Low']))
    # debug code
    if debug is True:
        print(listA)
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
