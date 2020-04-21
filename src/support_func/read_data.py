import pandas as pd
import configparser
#############################################################
# READING EXCEL and CREATING DATAFRAME
#############################################################

from support_func import severity as sv

############################################################
# Debug variable
debug_flag = True
############################################################

# Parsing input config file
config_rd = configparser.ConfigParser()


def read_config_file(path, config):
    """
        Args:
            config_file_name: path of file containing configuration parameters.
            objec to configParser
        Returns:
            Dictionary containing all parameters read from configuration file.
        Description:
            Read configuration data.
    """
    data = {}
    config.read(path)
    data['excel_path'] = config['input_params']['input_excel_path']

    return data


path = read_config_file('..\src\input.config', config_rd)

df = pd.read_excel(path['excel_path'])


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
                 "Gender","Did you travel out of PUNE after 1st March ?","What is the distance between office and place of residence ? (Approx. in KM )"]].drop_duplicates()

''' Renaming name of columns
'''
df_sel_col.columns = ['Name', 'ID', 'Team', 'Experience', 'Designation', 'Age', 'Gender','Travel_history','Home_distance']
######################################################################################################

##########################################################################################################
# Select only Specific Columns those which are required for advanced filter
##########################################################################################################

df_adv_col_in = df[["Your Name",
                    "Your Team", "Work Experience (Approx. in Years)", "Designation", "Age (In Years)","Gender",
                    "What is the distance between office and place of residence ? (Approx. in KM )",
                    "How many members are currently staying along with you ?",
                    "Have you come in contact with anyone with a travel history (within India/ abroad) ?",
                    "Are any of the people you are living with, allowed to work under Government regulations ?( Ex: Govt. servants, Healthcare personnel etc)",
                    "Have you come in contact with any person who tested POSITIVE for COVID-19 (directly/indirectly) ?",
                    "Did you travel out of PUNE after 1st March ?",
                    "Are you still staying at the same place?",
                    "When did you travel back to PUNE ?",
                    "Which mode of transportation did you use to travel back to PUNE ?",
                    ]]

df_adv_col_in.columns = ['Name', 'Team', 'Experience', 'Designation', 'Age', 'Gender', 'Distance', 'Members',
                         'Contact_Travel','Living_with_Govt_HealthCare', 'Contact_Covid', 'Travel out Pune',
                         'Stll There', 'When Came Back', 'Transportation']


#######################################################
# copy 1ast six columns from "df_adv_col_in"
#######################################################

df_adv_col_out = df_adv_col_in[['Name', 'Team', 'Experience', 'Designation', 'Age', 'Gender', 'Distance',
                                'Members']].copy()

df_adv_col_out['Health Risk'] = None
df_adv_col_out['Covid Contact Risk'] = None
df_adv_col_out['Covid Exposure Risk'] = None
df_adv_col_out['Travel Risk'] = None

# Above fields are None currently

##################################################################
# Update Output dataframe for advance tab
##################################################################
sv.eval_travel_risk_severity()

##################################################################
