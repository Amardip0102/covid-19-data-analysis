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
def calculate_designations_count(team, main_cat):
    listD = []
    if debug is True:
        print(team)
    df_designation = rd.df_sel_col.copy()
    if main_cat != 'All':
        is_mainteam = df_designation['Team_Category'] == main_cat
        df_designation = df_designation[is_mainteam]

    if team != 'All':
        is_team = df_designation['Team'] == team
        df_designation = df_designation[is_team]
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
def calculate_age_counts(team, main_cat):
    listA = []
    if debug is True:
        print(team)

    df_age = rd.df_sel_col.copy()
    if main_cat != 'All':
        is_mainteam = df_age['Team_Category'] == main_cat
        df_age = df_age[is_mainteam]

    if team != 'All':
        is_ageperteam = df_age['Team'] == team
        df_age = df_age[is_ageperteam]
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
def calculate_gender_count(team, main_cat):
    listG = []
    if debug is True:
        print(team)

    df_gender = rd.df_sel_col.copy()
    if main_cat != 'All':
        is_mainteam = df_gender['Team_Category'] == main_cat
        df_gender = df_gender[is_mainteam]

    if team != 'All':
        is_genderperteam = df_gender['Team'] == team
        df_gender = df_gender[is_genderperteam]
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

def calculate_Travel_count(team, main_cat):
    listG = []
    if debug is True:
        print(team)

    df_travel = rd.df_adv_col_out.copy()
    if main_cat != 'All':
        is_mainteam = df_travel['Team_Category'] == main_cat
        df_travel = df_travel[is_mainteam]

    if team != 'All':
        is_travelperteam = df_travel['Team'] == team
        df_travel = df_travel[is_travelperteam]
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
def calcWorkExperience(team, main_cat):
    if debug is True:
        print(team)
    listWE = []
    # ['Name', 'ID', 'Team', 'Experience', 'Designation', 'Age', 'Gender']
    df_work = rd.df_sel_col.copy()

    if main_cat != 'All':
        is_mainteam = df_work['Team_Category'] == main_cat
        df_work = df_work[is_mainteam]

    if team != 'All':
        is_work = df_work['Team'] == team
        df_work = df_work[is_work]
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
def calcWork_home_distance(team, main_cat):
    if debug is True:
        print(team)
    listWE = []
    # ['Name', 'ID', 'Team', 'Experience', 'Designation', 'Age', 'Gender']
    df_work = rd.df_adv_col_out.copy()
    if main_cat != 'All':
        is_mainteam = df_work['Team_Category'] == main_cat
        df_work = df_work[is_mainteam]

    if team != 'All':
        is_work = df_work['Team'] == team
        df_work = df_work[is_work]
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
def calculate_hotspot_exposure_counts(team, main_cat):
    listA = []
    if debug is True:
        print(team)

    df_rzone = rd.df_adv_col_out.copy()
    if main_cat != 'All':
        is_mainteam = df_rzone['Team_Category'] == main_cat
        df_rzone = df_rzone[is_mainteam]

    if team != 'All':
        is_rzoneperteam = df_rzone['Team'] == team
        df_rzone = df_rzone[is_rzoneperteam]
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
def calculate_covid_exposure_counts(team, main_cat):
    listA = []
    if debug is True:
        print(team)

    df_cvd= rd.df_adv_col_out.copy()
    if main_cat != 'All':
        is_mainteam = df_cvd['Team_Category'] == main_cat
        df_cvd = df_cvd[is_mainteam]

    if team != 'All':
        is_cvdperteam = df_cvd['Team'] == team
        df_cvd = df_cvd[is_cvdperteam]
    listA.append(len(df_cvd[df_cvd['Covid Contact Risk'] == 'High']))
    listA.append(len(df_cvd[df_cvd['Covid Contact Risk'] == 'Medium']))
    listA.append(len(df_cvd[df_cvd['Covid Contact Risk'] == 'Low']))
    # debug code
    if debug is True:
        print(listA)
    return listA
#############################################################


#############################################################
def calculate_staying_people_counts(team, main_cat):
    listA = []
    if debug is True:
        print(team)

    df_mem= rd.df_adv_col_out.copy()

    if main_cat != 'All':
        is_mainteam = df_mem['Team_Category'] == main_cat
        df_mem = df_mem[is_mainteam]

    if team != 'All':
        is_memperteam = df_mem['Team'] == team
        df_mem = df_mem[is_memperteam]
    listA.append(len(df_mem[df_mem['Members'] == filt.personcount['0-5 persons']]))
    listA.append(len(df_mem[df_mem['Members'] == filt.personcount['5-10 persons']]))
    listA.append(len(df_mem[df_mem['Members'] == filt.personcount['> 10 persons']]))
    # debug code
    if debug is True:
        print(listA)
    return listA
#############################################################


#############################################################
def calculate_health_risk_counts(team, main_cat):
    listA = []
    if debug is True:
        print(team)

    df_heal= rd.df_adv_col_out.copy()
    if main_cat != 'All':
        is_mainteam = df_heal['Team_Category'] == main_cat
        df_heal = df_heal[is_mainteam]

    if team != 'All':
        is_memperteam = df_heal['Team'] == team
        df_heal = df_heal[is_memperteam]
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

    # check main team
    if cache['Team_Category'] != 'All':
        is_mainteam = origdata['Team_Category'] == cache['Team_Category']
        origdata = origdata[is_mainteam]

    # check if team name is not All
    if cache['Team'] != 'All':
        is_team = origdata['Team'] == cache['Team']
        origdata = origdata[is_team]

    # check if designation is not all and filtering is required
    if cache['Designation'] != 'All':
        is_design = origdata['Designation'] == cache['Designation']
        origdata = origdata[is_design]

    # check if experience is not All
    if cache['Exp'] != 'All':
        is_exp = origdata['Experience'] == cache['Exp']
        origdata = origdata[is_exp]

    # check if gender is not all
    if cache['Gender'] != 'All':
        is_gender = origdata['Gender'] == cache['Gender']
        origdata = origdata[is_gender]

    # check if age is not All
    if cache['Age'] != 'All':
        is_age = origdata['Age'] == cache['Age']
        origdata = origdata[is_age]

    ###########################################################
    # Advance Filter: travel_risk, work_dist, living_with, redzone, covid_contact, health_risk,
    ###########################################################
    if travel_risk != 'All':
        is_travelRisk = origdata['Travel Risk'] == travel_risk
        origdata = origdata[is_travelRisk]

    # check if work_dist
    if work_dist != 'All':
        is_work_dist = origdata['Distance'] == work_dist
        origdata = origdata[is_work_dist]

    # check if living_with
    if living_with != 'All':
        is_member = origdata['Members'] == living_with
        origdata = origdata[is_member]

    #check if senior citizen kids
    if kids_srcitizen != 'All':
        is_kids_srcitizen = origdata['SrCitizen_Kids'] == kids_srcitizen
        origdata = origdata[is_kids_srcitizen]

    # check if office mode of transport
    if office_mode_transport != 'All':
        is_transportmode = origdata['Transport mode office'] == office_mode_transport
        origdata = origdata[is_transportmode]


    # check if redZOne Exposed
    if redzone != 'All':
        is_redZone = origdata['RedZone Exposure Risk'] == redzone
        origdata = origdata[is_redZone]

    # check if covid contact
    if covid_contact != 'All':
        is_covidContact = origdata['Covid Contact Risk'] == covid_contact
        origdata = origdata[is_covidContact]

    if health_risk != 'All':
        is_healthy = origdata['Health Risk'] == health_risk
        origdata = origdata[is_healthy]

    return origdata
