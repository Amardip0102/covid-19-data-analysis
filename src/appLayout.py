#############################################################
# Importing all module dependencies
#############################################################
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from tabs import basic_tab
from calc_counts import *
import read_data
#############################################################

############################################################
# Debug Variables
############################################################
debug = False
############################################################

app = dash.Dash(__name__)

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

        dcc.Tabs(id ='tab-app',value='basic-tab',children=[
            ################################################################################################
            # Basic Tab Content
            ################################################################################################
            dcc.Tab(label='Basic Filters', value='basic-tab',style=tab_style),
            ################################################################################################

            # Enter Different Tabs Section
            dcc.Tab(label='Advanced Filter', children=[], style=tab_style),
            dcc.Tab(label='Help', children=[],style=tab_style),
            dcc.Tab(label='About', children=[],style=tab_style),
        ], style=tabs_styles),
        html.Div(id='tabs-content-app')
], className='ten columns offset-by-one')


################################################################################################

#############################################################
# all callback functions to be designed here ...
#############################################################
@app.callback(
    dash.dependencies.Output('tabs-content-app', 'children'),
    [dash.dependencies.Input('tabs-app', 'value')])
def render_content(tab):
    if tab == 'basic-tab':
        return basic_tab.basic_layout
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
            'values': calc_counts.calcWorkExperience(team),
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
                'values': calc_counts.calculate_gender_count(team),
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
             'y': calc_counts.calculate_age_counts(team),
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
             'y': calc_counts.calculate_designations_count(team),
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
    out_df = read_data.df_sel_col.copy()
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
