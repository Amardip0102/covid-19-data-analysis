import pandas as pd
import configparser
#############################################################
# READING EXCEL and CREATING DATAFRAME
#############################################################

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
                 "Gender"]].drop_duplicates()

''' Renaming name of columns
'''
df_sel_col.columns = ['Name', 'ID', 'Team', 'Experience', 'Designation', 'Age', 'Gender']
######################################################################################################