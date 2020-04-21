from support_func import read_data as rd
############################################################
# Debug Variables
############################################################
debug = False
############################################################


#############################################################
# FUNCTION : calculate designations counts based on teams
#
#############################################################
def calculate_designations_count(team):
    listD = []
    if debug is True:
        print(team)
    df_designation = rd.df_sel_col.copy()
    if team != 'All':
        is_perteam = df_designation['Team'] == team
        df_designation = df_designation[is_perteam]
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
    if team != 'All':
        is_ageperteam = df_age['Team'] == team
        df_age = df_age[is_ageperteam]
    listA.append(len(df_age[df_age['Age'] == '20 - 30']))
    listA.append(len(df_age[df_age['Age'] == '30 - 40']))
    listA.append(len(df_age[df_age['Age'] == '40 - 50']))
    listA.append(len(df_age[df_age['Age'] == '> 50']))
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

def calculate_Travel_count(team):
    listG = []
    if debug is True:
        print(team)

    df_gender = rd.df_sel_col.copy()
    if team != 'All':
        is_genderperteam = df_gender['Team'] == team
        df_gender = df_gender[is_genderperteam]
    listG.append(len(df_gender[df_gender['Travel_history'] == 'Yes']))
    listG.append(len(df_gender[df_gender['Travel_history'] == 'No']))
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
    if team != 'All':
        is_work = df_work['Team'] == team
        df_work = df_work[is_work]
    listWE.append(len(df_work[df_work['Experience'] == '0 - 2']))
    listWE.append(len(df_work[df_work['Experience'] == '2 - 5']))
    listWE.append(len(df_work[df_work['Experience'] == '5 -10']))
    listWE.append(len(df_work[df_work['Experience'] == '> 10']))

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
    df_work = rd.df_sel_col.copy()
    if team != 'All':
        is_work = df_work['Team'] == team
        df_work = df_work[is_work]
    listWE.append(len(df_work[df_work['Home_distance'] == '0 - 5']))
    listWE.append(len(df_work[df_work['Home_distance'] == '6-10']))
    listWE.append(len(df_work[df_work['Home_distance'] == '10-15']))
    listWE.append(len(df_work[df_work['Home_distance'] == '>20']))

    # debug code
    if debug is True:
        print(listWE)
    return listWE
#############################################################