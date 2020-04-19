#############################################################
# Importing all module dependencies
#############################################################
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
#############################################################

############################################################
# Debug Variables
############################################################
debug = False
############################################################

app = dash.Dash(__name__)

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


#############################################################
# DATASET FOR ALL FILTERS SAME AS FORM
#############################################################
teamsList = {
            'All' : ['All'],
            'SupportFunctions': ['HR','ADMIN','SALES','FINANCE'],
            'IT+ToolsAndQuality': ['PMT','IT','QUALITY','INSTRU'],
            'advanceEngineering+2W/3W': ['AE-ML','AE','2W/3W'],
            'MechanicalDesign': ['MechanicalDesign'],
            'System_Fusa': ['SYSTEM/FuSa'],
            'software': ['SW-DEV-EST','SW-DEV-DIAG','SW-DEV-EPS','SW-DEV-GL','SW-DEV-VBS','SW-DEV-STAR3','SW-DEV-ADAS',
                          'SW-DEV-TBCM','SW-DEV-RPAS','SW-DEV-DCDC','SW-DEV-OTHER'],
            'SystemTesting': ['SYS_TEST-AudiSAR','SYS_TEST-STAR3','SYS_TEST-EPS','SYS_TEST-TATA','SYS_TEST-BCM2Evo',
                              'SYS_TEST-COBAS-VBS','SYS_TEST-RPAS','SYS-TEST-OTHER'],
            'hardware': ['HW-LAYOUT-LIBRARY','HW-DESIGN','HW-RADIO-HOMOLOGATION','HW-OTHER'],
            'others': ['OTHERS-NOT-LISTED']
            }

designations = ['All', 'Engineer', 'Sr. Engineer', 'Specialist', 'Sr.  Specialist', 'Tech/Team Lead', 'Dy. Manager', 'Manager',
                'Assistant Manager', 'Sr. Manager', 'Dy. Architect', 'Architect', 'Sr. Architect',
                'Dy. General Manager', 'General Manager', 'Other']


experience = {'All': 'All','0-2 Years': '0 - 2', '2-5 Years': '2 - 5', '5-10 Years':'5 -10', '> 10 Years': '> 10'}

age = {'All': 'All', '20-30 Years': '20 - 30', '30-40 Years': '30 - 40', '40-50 Years': '40 - 50', '> 50 Years': '> 50'}

gender = ['All', 'Male', 'Female', 'Other']
#############################################################

#############################################################
# Styling for Tab and Tables
#############################################################
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tabs_styles = {
    'height': '44px'
}

#  Layouts
layout_table = dict(
    autosize=True,
    height=500,
    font=dict(color="#191A1A"),
    titlefont=dict(color="#191A1A", size='14'),
    margin=dict(
        l=35,
        r=35,
        b=35,
        t=45
    ),
    hovermode="closest",
    plot_bgcolor='#fffcfc',
    paper_bgcolor='#fffcfc',
    legend=dict(font=dict(size=10), orientation='h'),
)
layout_table['font-size'] = '12'
layout_table['margin-top'] = '20'
layout_table['border'] = '2px solid black',
##############################################################


#############################################################
# FUNCTION : calculate designations counts based on teams
#
#############################################################
def calculate_designations_count(team):
    listD = []
    if debug is True:
        print(team)
    df_designation = df_sel_col.copy()
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

    df_age = df_sel_col.copy()
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

    df_gender = df_sel_col.copy()
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
# FUNCTION : calculate work experience counts based on teams
#
#############################################################
def calcWorkExperience(team):
    if debug is True:
        print(team)
    listWE = []
    # ['Name', 'ID', 'Team', 'Experience', 'Designation', 'Age', 'Gender']
    df_work = df_sel_col.copy()
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
# APPLICATION LAYOUT IS HERE .....
#############################################################
app.layout = html.Div([
        # Start : Heading of the report
        #####################################################
        html.Div([
            html.H1(children='POST COVID 19 EVALUATION DASHBOARD RESULT',
                    style={
                        'textAlign': 'center',
                        'color': 'black',
                        'font-weight': 'bold'
                    }
                    ),
            html.Div(children='HELLA India Automotive Pvt. Ltd',
                     style={
                         'textAlign': 'center',
                         'color': '#0000ff'
                     }
                     )
        ], className="row"),
        html.Div([
            html.H1(children='----------------------------------------------------------------------------------------',
                    style={
                        'textAlign': 'center',
                        'color': 'black'
                    }
                    ),
        ], className= "row"),
        # End : Heading of the report
        #############################################################

        #############################################################
        html.Div([
            html.H3(children='Filters',
                    style={
                        'textAlign': 'left',
                        'color': 'blue',
                        'font-weight': 'bold'
                    })
        ], className='row'),
        #############################################################

        dcc.Tabs([
            ################################################################################################
            # Basic Tab Content
            ################################################################################################
            dcc.Tab(label='Basic Filters', children=[
                #############################################################
                # Start: Basic Filter Options
                html.Div([
                    ##############################################################
                    # First Four Columns
                    ##############################################################
                    html.Div([
                        html.Label(
                            children = 'Team Category',
                            style={'color': 'black','font-weight': 'bold'}
                        ),
                        dcc.Dropdown(
                            id='team-cat-dropdown',
                            options=[{'label': v, 'value': v} for v in teamsList.keys()],
                            value='All'
                        ),

                        html.Label(
                            'Select Specific Team',
                            style={'color': 'black', 'font-weight': 'bold'}
                        ),
                        dcc.Dropdown(
                            id = 'spec-team-dropdown',
                            options=[{'label': v[i], 'value': v[i]} for k,v in teamsList.items() for i in range(len(v))],
                            value='All',
                            multi=False
                        )
                    ], className="four columns"),
                    ##############################################################


                    ##############################################################
                    #   Four Columns
                    ##############################################################
                    html.Div([
                        html.Label(
                            'Select Designations',
                            style={'color': 'black', 'font-weight': 'bold'}
                        ),
                        dcc.Dropdown(
                            id = 'designation-dropdown',
                            options=[{'label': k, 'value': k} for k in designations],
                            value='All',
                            disabled=False,
                            multi=False
                        ),

                        html.Label(
                            'Experience',
                            style={'color': 'black', 'font-weight': 'bold'}
                        ),
                        dcc.Dropdown(
                            id = 'exp-dropdown',
                            options=[{'label': k, 'value': v} for k,v in experience.items()],
                            value='All',
                            disabled=False,
                            multi=False
                        )
                    ], className="four columns"),
                    ##############################################################

                    ##############################################################
                    # Four Columns
                    ##############################################################
                    html.Div([
                        html.Label(
                            'Gender',
                            style={'color': 'black', 'font-weight': 'bold'}
                        ),
                        dcc.Dropdown(
                            id = 'gender-dropdown',
                            options=[{'label': k, 'value': k} for k in gender],
                            value='All',
                            disabled=False,
                            multi=False
                        ),

                        html.Label(
                            'Age',
                            style={'color': 'black', 'font-weight': 'bold'}
                        ),
                        dcc.Dropdown(
                            id = 'age-dropdown',
                            options=[{'label': k, 'value': v} for k,v in age.items()],
                            value='All',
                            disabled=False,
                            multi=False
                        )
                    ], className="four columns")
                    ##############################################################
                ], style={"border":"2px black solid"},className="row"),
                # end : basic filters here
                #############################################################

                #############################################################
                html.Div([
                    html.H3(children='Charts and Graphs',
                            style={
                                'textAlign': 'left',
                                'color': 'blue',
                                'font-weight': 'bold'
                            })
                ], className='row'),
                #############################################################

                #############################################################
                # plotting graphs from here onwards
                html.Div([
                    html.Div([
                        dcc.Graph(
                            id = 'designations-Id',
                            figure={
                                'data' : [
                                    {'x':['Engineer', 'Sr. Engineer', 'Specialist', 'Sr. Specialist', 'Tech-Team Lead',
                                          'Dy. Manager', 'Manager','Assistant Manager', 'Sr. Manager', 'Dy. Architect',
                                          'Architect', 'Sr. Architect','Dy. General Manager', 'General Manager', 'Other'],
                                     'y':calculate_designations_count('All'),
                                     'type': 'bar'},
                                ],
                                'layout': {
                                    # experiment and finalise colors
                                    # 'plot_bgcolor': '#90EE90',
                                    # 'paper_bgcolor': '#90EE90',
                                    'font' : {
                                        'color' : 'black'
                                    },
                                    'title': 'Designations'
                                }
                            }
                        )
                    ], className='six columns'),

                    html.Div([
                        dcc.Graph(
                            id = 'work-exp',
                            figure={
                                'data' :[
                                    {
                                        'values': calcWorkExperience('All'),
                                        'type': 'pie',
                                        'name': 'WorkExp',
                                        "labels": ['0-2 Years', '2-5 Years', '5-10 Years', '> 10 years'],
                                    }],
                                'layout': {
                                        'font' : {
                                            'color' : 'black'
                                        },
                                        'title': 'Work Experience',
                                }
                            },
                        )
                    ], className ='six columns'),

                    html.Div([
                        dcc.Graph(
                            id='gender-pie',
                            figure={
                                'data': [
                                    {
                                        'values': calculate_gender_count('All'),
                                        'type': 'pie',
                                        'name': 'genderPie',
                                        "labels": ['Male', 'Female', 'Others'],
                                    }],
                                'layout': {
                                    'font': {
                                        'color': 'black'
                                    },
                                    'title': 'Gender Wise Distribution',
                                }
                            },
                        )
                    ], className='six columns'),

                    html.Div([
                        dcc.Graph(
                            id = 'age-Id',
                            figure={
                                'data' : [
                                    {'x':['20-30 Years', '30-40 Years', '40-50 Years', '> 50 Years'],
                                     'y':calculate_age_counts('All'),
                                     'type': 'bar'},
                                ],
                                'layout': {
                                    # experiment and finalise colors
                                    # 'plot_bgcolor': '#90EE90',
                                    # 'paper_bgcolor': '#90EE90',
                                    'font' : {
                                        'color' : 'black'
                                    },
                                    'title': 'Age Wise Distribution'
                                }
                            }
                        )
                    ], className='five columns'),
                ], style={"border":"2px black solid"},className="row"),
                #############################################################
                html.Div([
                    html.H3(children='Display Data',
                            style={
                                'textAlign': 'left',
                                'color': 'blue',
                                'font-weight': 'bold'
                            })
                ], className='row'),
                #############################################################
                html.Div([
                    dash_table.DataTable(
                        id='table',
                        columns=[{"name": i, "id": i} for i in df_sel_col.columns],
                        data=df_sel_col.to_dict("rows"),
                        editable=False,
                        # scroll enabled
                        style_table={'maxWidth': '1500px','overflowY': 'scroll', 'maxHeight': '400px','border': 'thin lightgrey solid'},
                        style_cell_conditional=[
                            {'if': {'column_id': 'Name'},
                             'width': '25%'},
                            {'if': {'column_id': 'ID'},
                             'width': '10%'},
                            {'if': {'column_id': 'Team'},
                             'width': '20%'},
                            {'if': {'column_id': 'Designation'},
                             'width': '15%'},
                        ],
                        row_selectable="multi",
                        selected_rows=[0],
                        style_cell={"fontFamily": "Arial", "size": 15, 'textAlign': 'center'},
                        style_data={'border': '1px solid blue'},
                        style_header={'border': '2px solid black'},
                        # freeze header row when scrolling
                        fixed_rows={'headers': True},
                        # sorting data in table
                        sort_action="native",
                        sort_mode="single",
                    )
                ],
                style = layout_table,
                className=" twelve columns"),
            ],style=tab_style),
            ################################################################################################

            # Enter Different Tabs Section
            dcc.Tab(label='Advanced Filter', children=[

            ], style=tab_style),
            dcc.Tab(label='Help', children=[],style=tab_style),
            dcc.Tab(label='About', children=[],style=tab_style),
        ], style=tabs_styles)
], className='ten columns offset-by-one')


################################################################################################

#############################################################
# all callback functions to be designed here ...
#############################################################
#############################################################
# start: callback for updating teams based on main team categories
#############################################################
@app.callback(
    dash.dependencies.Output('spec-team-dropdown', 'options'),
    [dash.dependencies.Input('team-cat-dropdown', 'value')]
)
def update_spc_team_dropdown(name):
    return [{'label': i, 'value': i} for i in teamsList[name]]
#############################################################


#############################################################
# callback for updating work experience as per teams
#############################################################
@app.callback(
    dash.dependencies.Output('work-exp', 'figure'),
    [dash.dependencies.Input('spec-team-dropdown', 'value')]
)
def update_work_experience(team):

    return {
        'data': [
        {
            'values': calcWorkExperience(team),
            'type': 'pie',
            'name': 'WorkExp',
            "labels": ['0-2 Years', '2-5 Years', '5-10 Years', '> 10 years']
        }],
        'layout': {
            'font': {
                'color': 'black',
            },
            'title': 'Work Experience'
        }
    }
########################################################################


#############################################################
# callback for updating gender as per teams
#############################################################
@app.callback(
    dash.dependencies.Output('gender-pie', 'figure'),
    [dash.dependencies.Input('spec-team-dropdown', 'value')]
)
def update_gender(team):

    return {
        'data': [
            {
                'values': calculate_gender_count(team),
                'type': 'pie',
                'name': 'genderPie',
                "labels": ['Male', 'Female', 'Others'],
            }],
        'layout': {
            'font': {
                'color': 'black'
            },
            'title': 'Gender Wise Distribution',
        }
    }
########################################################################


#######################################################################
# Callback function for updating Age Wise Count
#######################################################################
@app.callback(
    dash.dependencies.Output('age-Id', 'figure'),
    [dash.dependencies.Input('spec-team-dropdown', 'value')]
)
def update_age(team):

    return {
        'data': [
            {'x': ['20-30 Years', '30-40 Years', '40-50 Years', '> 50 Years'],
             'y': calculate_age_counts(team),
             'type': 'bar'},
        ],
        'layout': {
            # experiment and finalise colors
            # 'plot_bgcolor': '#90EE90',
            # 'paper_bgcolor': '#90EE90',
            'font': {
                'color': 'black'
            },
            'title': 'Age Wise Distribution'
        }
    }
########################################################################


#######################################################################
# Callback Function for Designation Updates
#######################################################################
@app.callback(
    dash.dependencies.Output('designations-Id', 'figure'),
    [dash.dependencies.Input('spec-team-dropdown', 'value')]
)
def update_gender(team):
    return {
        'data': [
            {'x': ['Engineer', 'Sr. Engineer', 'Specialist', 'Sr. Specialist', 'Tech-Team Lead',
                   'Dy. Manager', 'Manager', 'Assistant Manager', 'Sr. Manager', 'Dy. Architect',
                   'Architect', 'Sr. Architect', 'Dy. General Manager', 'General Manager', 'Other'],
             'y': calculate_designations_count(team),
             'type': 'bar'},
        ],
        'layout': {
            # experiment and finalise colors
            # 'plot_bgcolor': '#90EE90',
            # 'paper_bgcolor': '#90EE90',
            'font': {
                'color': 'black'
            },
            'title': 'Designations'
        }
    }
########################################################################
########################################################################
# Update callback : Table
########################################################################
@app.callback(
    dash.dependencies.Output('table', 'data'),
    [dash.dependencies.Input('spec-team-dropdown', 'value'),
     dash.dependencies.Input('designation-dropdown', 'value'),
     dash.dependencies.Input('gender-dropdown', 'value'),
     dash.dependencies.Input('age-dropdown', 'value'),
     dash.dependencies.Input('exp-dropdown', 'value')]
)
def update_table(team_name, design_name, gender, age, exp):
    # create a copy of main data here
    out_df = df_sel_col.copy()
    # print(out_df.head(5))
    # ['Name', 'ID', 'Team', 'Experience', 'Designation', 'Age', 'Gender'] for reference

    # check if team name is not All
    if team_name != 'All':
        is_team = out_df['Team'] == team_name
        out_df = out_df[is_team]

    # check if designation is not all and filtering is required
    if design_name != 'All':
        is_design = out_df['Designation'] == design_name
        out_df = out_df[is_design]

    # check if experience is not All
    if exp != 'All':
        is_exp = out_df['Experience'] == exp
        out_df = out_df[is_exp]

    # check if gender is not all
    if gender != 'All':
        is_gender = out_df['Gender'] == gender
        out_df = out_df[is_gender]

    # check if age is not All
    if age != 'All':
        is_age = out_df['Age'] == age
        out_df = out_df[is_age]

    data = out_df.to_dict("rows")
    return data
########################################################################


########################################################################
# Start Server Here
########################################################################
if __name__ == '__main__':
    app.run_server(debug=True)
