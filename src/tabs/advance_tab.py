#############################################################
# Importing all module dependencies
#############################################################
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from support_func import filtering
from support_func import calc_counts
from support_func import read_data
#############################################################

advance_layout = html.Div([

   html.Div([
        ##############################################################
        # First Four Columns
        ##############################################################

        html.Div(
            [
                html.Label(
                    children='Travel risk severity',
                    style={'color': 'black', 'font-weight': 'bold'}
                ),
                dcc.Dropdown(
                    id='travel_risk_severity',
                    options=[{'label': k, 'value': k} for k in filtering.severity],
                    value= 'All',
                    multi=False
                ),

                html.Label(
                    'Exposure Severity to affected areas ',
                    style={'color': 'black', 'font-weight': 'bold'}
                ),
                dcc.Dropdown
                    (
                    id='exposure_affected_severity',
                    options=[{'label': k, 'value': k} for k in filtering.severity],
                    value= 'All',
                    multi=False
                ),

                html.Label(
                    'Reset Filters to ALL',
                    style={'color': 'black', 'font-weight': 'bold'}
                ),
                html.Button(
                    'Reset Button',
                    style={'color': 'black', 'font-weight': 'bold', 'width': '100%', 'display': 'table-cell'},
                    id='reset-adv-filter-button',
                    type='submit',
                    n_clicks=0
                )
            ], className="four columns"),

        #####################################################################
        #   Four Columns
        ##############################################################
        html.Div([
            html.Label(
                'Office to home Travel distance',
                style={'color': 'black', 'font-weight': 'bold'}
            ),
            dcc.Dropdown(
                id='distance-dropdown',
                options=[{'label': k, 'value': v} for k, v in filtering.distance.items()],
                value='All',
                multi=False
            ),

            html.Label(
                'Contact with covid19 severity',
                style={'color': 'black', 'font-weight': 'bold'}
            ),
            dcc.Dropdown(
                id='severity-dropdown',
                options=[{'label': k, 'value': k} for k in filtering.severity],
                value='All',
                multi=False
            ),

            html.Label(
                children='Sr Citizen / Kids',
                style={'color': 'black', 'font-weight': 'bold'}
            ),
            dcc.Dropdown(
                id='sr-cit-kids',
                options=[{'label': v, 'value': v} for v in filtering.srCitizensKids],
                value='All'
            )
        ], className="four columns"),
        ##############################################################
        html.Div(
            [
                html.Label(
                    children='Health Condition Severity',
                    style={'color': 'black', 'font-weight': 'bold'}
                ),
                dcc.Dropdown(
                    id='health_risk_severity',
                    options=[{'label': k, 'value': k} for k in filtering.severity],
                    value = 'All',
                    multi=False
                ),

                html.Label(
                    'Living with Number of people',
                    style={'color': 'black', 'font-weight': 'bold'}
                ),
                dcc.Dropdown
                    (
                    id='people-living-count',
                    options=[{'label': k, 'value': v} for k, v in filtering.personcount.items()],
                    value='All',
                    multi=False

                )
            ], className="four columns"),
        ##############################################################

        # end : Advanced filters here
        #############################################################
    ], style={"border": "2px black solid"}, className="row"),
    #############################################################

    html.Div([
        html.Div([
            html.H5(
                id='data-processed-text-adv',
                children='Data processed using Basic+Advanced: ',
                style={
                    'textAlign': 'left',
                    'color': 'blue',
                    'font-weight': 'bold'}
            )
        ]),

        html.Div([
            html.H5(
                id='data-processed-count-adv',
                children=' 0 Employees',
                style={
                    'textAlign': 'left',
                    'color': 'red',
                    'font-weight': 'bold'}
            )
        ])

    ], style={"border": "2px black solid"}, className="row"),

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

    # plotting graphs from here onwards
    html.Div([
        html.Div([
            dcc.Graph(
                id='travel-severity',
                figure={
                    'data': [
                        {
                            'values': calc_counts.calculate_Travel_count('All'),
                            'type': 'pie',
                            'name': 'Travel Severity',
                            "labels": ['High', 'Medium','Low'],
                        }],
                    'layout': {
                        'font': {
                            'color': 'black'
                        },
                        'title': 'Travel Risk Distribution',
                    }
                },
            )
        ], className='six columns'),

        html.Div([
            dcc.Graph(
                id='work-distance',
                figure={
                    'data': [
                        {
                            'x': ['0-5 Km', '5-10 kms', '10-15 kms','15-20 kms', '> 20 Kms'],
                            'y': calc_counts.calcWork_home_distance('All'),
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
            )
        ], className='five columns'),

        html.Div([
            dcc.Graph(
                id='living-with',
                figure={
                    'data': [
                        {'x': ['0-5 members', '5-10 members', '>10 members'],
                         'y': calc_counts.calculate_staying_people_counts('All'),
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
                }
            )
        ], className='five columns'),

        html.Div([
            dcc.Graph(
                id='redzone-exposure',
                figure={
                    'data': [
                      {
                         'values': calc_counts.calculate_hotspot_exposure_counts('All'),
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
                }
            )
        ], className='six columns'),

        html.Div([
            dcc.Graph(
                id='covid-exposure',
                figure={
                    'data': [
                         {
                         'values': calc_counts.calculate_covid_exposure_counts('All'),
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
                }
            )
        ], className='six columns'),

        html.Div([
            dcc.Graph(
                id='health',
                figure={
                    'data': [
                        {'x': ['High', 'Medium', 'Low'],
                         'y': calc_counts.calculate_health_risk_counts('All'),
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
            )
        ], className='five columns'),

     ], style={"border": "2px black solid"}, className="row"),
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

    #############################################################
    # Plotting a table
    #############################################################
    html.Div([
        dash_table.DataTable(
            id='table-adv',
            columns=[{"name": i, "id": i} for i in read_data.df_adv_col_out.loc[:,['Name','ID','Team','Distance',
                                                                                   'Members', 'SrCitizen_Kids',
                                                                                   'Health Risk', 'Covid Contact Risk',
                                                                                   'RedZone Exposure Risk',
                                                                                   'Travel Risk']]],
            data=read_data.df_adv_col_out.to_dict("rows"),
            editable=False,
            # scroll enabled
            style_table={'maxWidth': '1500px', 'overflowY': 'scroll', 'maxHeight': '400px',
                         'border': 'thin lightgrey solid'},
            style_cell_conditional=[
                {'if': {'column_id': 'Name'},
                 'width': '10%'},
                {'if': {'column_id': 'ID'},
                 'width': '10%'},
                {'if': {'column_id': 'Team'},
                 'width': '10%'},
                {'if': {'column_id': 'Designation'},
                 'width': '10%'},
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
            export_format = 'xlsx'
        )
    ],
        style=filtering.layout_table,
        className=" twelve columns")
    ######################################################################################

])