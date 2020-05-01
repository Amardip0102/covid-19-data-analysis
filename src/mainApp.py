#############################################################
# Importing all module dependencies
#############################################################
import dash
import dash_auth
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from tabs import basic_tab
from tabs import advance_tab
from tabs import about
from tabs import help
from support_func import calc_counts
from support_func import read_data
from support_func import filtering
#############################################################


############################################################
# Debug Variables
############################################################
debug = False
production = False
############################################################

############################################################
# Organization Name
############################################################
org_name = "HELLA India Automotive Pvt. Ltd. Pune"
############################################################
VALID_USERNAME_PASSWORD_PAIRS = {
    read_data.username: read_data.password
}

if production:
    from flask import Flask
    server = Flask(__name__)
    app = dash.Dash(__name__, server=server)
else:
    app = dash.Dash(__name__)

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)
#############################################################

app.config['suppress_callback_exceptions'] = True
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
            html.H1(children='POST LOCK DOWN EVALUATION DASHBOARD',
                    style={
                        'textAlign': 'center',
                        'color': 'black',
                        'font-weight': 'bold'
                    }
                    ),

            html.Div([
                html.H2(children=org_name,
                     style={
                         'textAlign': 'center',
                         'color': '#0000ff'
                     }
                )
            ])
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

        dcc.Store(id='shared-dropdown-data',  data={'Team': 'All', 'Designation': 'All',
                                                    'Gender': 'All', 'Age': 'All', 'Exp': 'All'}),

        dcc.Tabs(id ='tab-app',value='basic-tab',children=[
            ################################################################################################
            # Basic Tab Content
            ################################################################################################
            dcc.Tab(label='Basic Filters', children=basic_tab.basic_layout,value='basic-tab',style=tab_style),
            ################################################################################################

            # Enter Different Tabs Section
            dcc.Tab(label='Advanced Filter',children=advance_tab.advance_layout, value='advance-tab', style=tab_style),
            dcc.Tab(label='Help', children=help.help_layout, value='help-tab', style=tab_style),
            dcc.Tab(label='About', children=about.about_layout, value='about-tab',style=tab_style),
        ], style=tabs_styles),
        html.Div(id='tabs-content-app')
], className='ten columns offset-by-one')


################################################################################################

#############################################################
# all callback functions to be designed here ...
#############################################################

#############################################################
# CallBack for rendering entire application..
#############################################################
'''
@app.callback(
    dash.dependencies.Output('tabs-content-app', 'children'),
    [dash.dependencies.Input('tab-app', 'value')])
def render_content(tab):
    if tab == 'basic-tab':
        return basic_tab.basic_layout
    elif tab == 'advance-tab':
        return advance_tab.advance_layout
    elif tab == 'help-tab':
        return help.help_layout
    elif tab == 'about-tab':
        return about.about_layout
'''

#############################################################
#
############################################################
@app.callback(
    dash.dependencies.Output('shared-dropdown-data', 'data'),
    [dash.dependencies.Input('spec-team-dropdown', 'value'),
     dash.dependencies.Input('designation-dropdown', 'value'),
     dash.dependencies.Input('gender-dropdown', 'value'),
     dash.dependencies.Input('age-dropdown', 'value'),
     dash.dependencies.Input('exp-dropdown', 'value')],
    [dash.dependencies.State('tab-app', 'value')],
)
def update_dropdown_cache(team, designation, gender, age, exp, tabval):
    data = {}
    if tabval == 'basic-tab':
        data['Team'] = team
        data['Designation'] = designation
        data['Gender'] = gender
        data['Age'] = age
        data['Exp'] = exp
    if debug is True:
        print(data)
    return data


#############################################################
# start: callback for updating teams based on main team categories
#############################################################
@app.callback(
    dash.dependencies.Output('spec-team-dropdown', 'options'),
    [dash.dependencies.Input('team-cat-dropdown', 'value')]
)
def update_spc_team_dropdown(name):
    return [{'label': i, 'value': i} for i in filtering.teamsList[name]]
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
    [dash.dependencies.Output('table', 'data'),
    dash.dependencies.Output('data-processed-count', 'children')],
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

    return data, str(len(out_df.index)) + ' Employees'
########################################################################


########################################################################
# Update callback : table-adv
########################################################################
@app.callback(
    [dash.dependencies.Output('table-adv', 'data'),
     dash.dependencies.Output('data-processed-count-adv', 'children')],
    [dash.dependencies.Input('travel_risk_severity', 'value'),
     dash.dependencies.Input('distance-dropdown', 'value'),
     dash.dependencies.Input('people-living-count', 'value'),
     dash.dependencies.Input('sr-cit-kids', 'value'),
     dash.dependencies.Input('office-mode-transport', 'value'),
     dash.dependencies.Input('exposure_affected_severity', 'value'),
     dash.dependencies.Input('severity-dropdown', 'value'),
     dash.dependencies.Input('health_risk_severity', 'value'),
     dash.dependencies.Input('tab-app', 'value')],
    [dash.dependencies.State('shared-dropdown-data', 'data')]
)
def update_advance_table(travel_risk, work_dist, living_with, kids_srcitizen, office_mode_transport, redzone, covid_contact, health_risk, tab, cache):
    adv_out_df = read_data.df_adv_col_out.copy()

    adv_out_df = calc_counts.filter_advance_data(adv_out_df, travel_risk, work_dist, living_with, kids_srcitizen,office_mode_transport,
                                                 redzone, covid_contact, health_risk, cache)

    data = adv_out_df.to_dict("rows")

    return data, str(len(adv_out_df.index)) + ' Employees'

########################################################################
# App Callback: Button
########################################################################
@app.callback(
    [dash.dependencies.Output('spec-team-dropdown', 'value'),
    dash.dependencies.Output('team-cat-dropdown', 'value'),
    dash.dependencies.Output('designation-dropdown', 'value'),
    dash.dependencies.Output('gender-dropdown', 'value'),
    dash.dependencies.Output('age-dropdown', 'value'),
    dash.dependencies.Output('exp-dropdown', 'value')],
    [dash.dependencies.Input('reset-filter-button', 'n_clicks')]
)
def update_filter(reset_btn):
    return 'All', 'All', 'All', 'All', 'All', 'All'

########################################################################
# App Callback: reset-adv-filter-button
# id='travel_risk_severity', id='exposure_affected_severity', id='distance-dropdown', id='severity-dropdown',
# id='health_risk_severity', id='people-living-count'
########################################################################
@app.callback(
    [dash.dependencies.Output('travel_risk_severity', 'value'),
     dash.dependencies.Output('exposure_affected_severity', 'value'),
     dash.dependencies.Output('distance-dropdown', 'value'),
     dash.dependencies.Output('severity-dropdown', 'value'),
     dash.dependencies.Output('health_risk_severity', 'value'),
     dash.dependencies.Output('people-living-count', 'value'),
     dash.dependencies.Output('sr-cit-kids', 'value'),
     dash.dependencies.Output('office-mode-transport', 'value')],
    [dash.dependencies.Input('reset-adv-filter-button', 'n_clicks')]
)
def reset_adv_filter(adv_reset):
    return ['All'], ['All'], ['All'], ['All'], ['All'], ['All'], 'All', ['All']

#######################################################################

@app.callback(
    [dash.dependencies.Output('travel-severity', 'figure'),
     dash.dependencies.Output('work-distance', 'figure'),
     dash.dependencies.Output('living-with', 'figure'),
     dash.dependencies.Output('redzone-exposure', 'figure'),
     dash.dependencies.Output('covid-exposure', 'figure'),
     dash.dependencies.Output('health', 'figure')],
    [dash.dependencies.Input('shared-dropdown-data', 'data')]
)
def update_Advancefilter_figures(data):
    return [
        {
        'data': [
            {
                'values': calc_counts.calculate_Travel_count(data['Team']),
                'type': 'pie',
                'name': 'Travel Severity',
                "labels": ['High', 'Medium', 'Low'],
            }],
        'layout': {
            'font': {
                'color': 'black'
            },
            'title': 'Travel Risk Distribution',
        }

       },

       {
            'data': [
                {
                    'x': ['0-5 Km', '5-10 kms', '10-15 kms','15-20 kms', '> 20 Kms'],
                    'y': calc_counts.calcWork_home_distance(data['Team']),
                    'type': 'bar'
                },
            ],
            'layout': {
                'font': {
                    'color': 'black'
                },
                'title': 'Work-Home Distance Distribution',
            }
        },

        {
            'data': [
                {'x': ['0-5 members', '5-10 members', '>10 members'],
                 'y': calc_counts.calculate_staying_people_counts(data['Team']),
                 'type': 'bar'},
            ],
            'layout': {
                # experiment and finalise colors
                # 'plot_bgcolor': '#90EE90',
                # 'paper_bgcolor': '#90EE90',
                'font': {
                    'color': 'black'
                },
                'title': 'Members Staying With Distribution'
            }
        },


        {
            'data': [
                {
                    'values': calc_counts.calculate_hotspot_exposure_counts(data['Team']),
                    'type': 'pie',
                    'name': 'Red Zone exposure Severity',
                    'labels': ['High', 'Medium', 'Low'],

                },
            ],
            'layout': {
                # experiment and finalise colors
                # 'plot_bgcolor': '#90EE90',
                # 'paper_bgcolor': '#90EE90',
                'font': {
                    'color': 'black'
                },
                'title': 'RedZone Exposed Employees '
            }
        },

        {
            'data': [
                {
                    'values': calc_counts.calculate_covid_exposure_counts(data['Team']),
                    'type': 'pie',
                    'name': 'Red Zone exposure Severity',
                    'labels': ['High', 'Medium', 'Low'],
                },
            ],
            'layout': {
                # experiment and finalise colors
                # 'plot_bgcolor': '#90EE90',
                # 'paper_bgcolor': '#90EE90',
                'font': {
                    'color': 'black'
                },
                'title': 'Covid19 Contact Risk Employees'
            }
        },

        {
            'data': [
                {'x': ['High', 'Medium', 'Low'],
                 'y': calc_counts.calculate_health_risk_counts(data['Team']),
                 'type': 'bar'},
            ],
            'layout': {
                # experiment and finalise colors
                # 'plot_bgcolor': '#90EE90',
                # 'paper_bgcolor': '#90EE90',
                'font': {
                    'color': 'black'
                },
                'title': 'Health risk assessment '
            }
       }

    ]


#######################################################################
########################################################################
# Start Server Here
########################################################################
if __name__ == '__main__':
    app.run_server(debug=True)
