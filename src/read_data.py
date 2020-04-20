import pandas as pd
#############################################################
# READING EXCEL and CREATING DATAFRAME
#############################################################
path_excel='C:\\Users\\ghodam2\\Downloads\\POST-COVID19_(1-10).xlsx'
df = pd.read_excel(path_excel)


#############################################################
# Fetch Indexes from Specified Columns
#############################################################
TEAM_NAME_IDX   = df.columns.get_loc("Your Team")
DESIGNATION_IDX = df.columns.get_loc("Designation")
AGE_IDX         = df.columns.get_loc("Age (In Years)")
GENDER_IDX      = df.columns.get_loc("Gender")
WORK_EXP_IDX    = df.columns.get_loc("Work Experience (Approx. in Years)")
#############################################################

##########################################################################################################
# Select only Specific Columns those which are required
##########################################################################################################
df_sel_col = df[["Your Name", "Employee ID (e.g. HEDCI-123) (Please put ID number only in this case 123 )",
                 "Your Team", "Work Experience (Approx. in Years)", "Designation", "Age (In Years)",
                 "Gender"]].drop_duplicates()

''' Renaming name of columns
'''
df_sel_col.columns = ['Name', 'ID', 'Team', 'Experience', 'Designation', 'Age', 'Gender']
######################################################################################################