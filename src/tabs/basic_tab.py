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
# Start: Basic Filter Options
############################################################
basic_layout = html.Div([
    html.Div([
        ##############################################################
        # First Four Columns
        ##############################################################
        html.Div([
            html.Label(
                children='Team Category',
                style={'color': 'black', 'font-weight': 'bold'}
            ),
            dcc.Dropdown(
                id='team-cat-dropdown',
                options=[{'label': v, 'value': v} for v in filtering.teamsList.keys()],
                value='All'
            ),

            html.Label(
                'Select Specific Team',
                style={'color': 'black', 'font-weight': 'bold'}
            ),
            dcc.Dropdown(
                id='spec-team-dropdown',
                options=[{'label': v[i], 'value': v[i]} for k, v in filtering.teamsList.items() for i in range(len(v))],
                value=['All'],
                multi=True
            ),

            html.Label(
                'Reset Filters to ALL',
                style={'color': 'black', 'font-weight': 'bold'}
            ),
            html.Button(
                'Reset Button',
                style={'color': 'black', 'font-weight': 'bold','width': '100%','display':'table-cell'},
                id='reset-filter-button',
                type = 'submit',
                n_clicks=0
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
                id='designation-dropdown',
                options=[{'label': k, 'value': k} for k in filtering.designations],
                value=['All'],
                disabled=False,
                multi=True
            ),

            html.Label(
                'Experience',
                style={'color': 'black', 'font-weight': 'bold'}
            ),
            dcc.Dropdown(
                id='exp-dropdown',
                options=[{'label': k, 'value': v} for k, v in filtering.experience.items()],
                value=['All'],
                disabled=False,
                multi=True
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
                id='gender-dropdown',
                options=[{'label': k, 'value': k} for k in filtering.gender],
                value=['All'],
                disabled=False,
                multi=True
            ),

            html.Label(
                'Age',
                style={'color': 'black', 'font-weight': 'bold'}
            ),
            dcc.Dropdown(
                id='age-dropdown',
                options=[{'label': k, 'value': v} for k, v in filtering.age.items()],
                value=['All'],
                disabled=False,
                multi=True
            )
        ], className="four columns"),
        ##############################################################
    ], style={"border": "2px black solid"}, className="row"),
    # end : basic filters here
    #############################################################

    html.Div([
        html.Div([
            html.H5(
                id='data-processed-text',
                children='Data processed using this filter: ',
                style={
                    'textAlign': 'left',
                    'color': 'blue',
                    'font-weight': 'bold'}
            )
        ]),

        html.Div([
            html.H5(
                id='data-processed-count',
                children=' 0 Employees',
                style={
                    'textAlign': 'left',
                    'color': 'red',
                    'font-weight': 'bold'}
            )
        ])

    ], style={"border": "2px black solid"}, className="row"),

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
                id='designations-Id',
                figure={
                    'data': [
                        {'x': ['Engineer', 'Sr. Engineer', 'Specialist', 'Sr. Specialist', 'Tech-Team Lead',
                               'Dy. Manager', 'Manager', 'Assistant Manager', 'Sr. Manager', 'Dy. Architect',
                               'Architect', 'Sr. Architect', 'Dy. General Manager', 'General Manager', 'Other'],
                         'y': calc_counts.calculate_designations_count(read_data.df_sel_col),
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
            )
        ], className='six columns'),

        html.Div([
            dcc.Graph(
                id='work-exp',
                figure={
                    'data': [
                        {
                            'values': calc_counts.calcWorkExperience(read_data.df_sel_col),
                            'type': 'pie',
                            'name': 'WorkExp',
                            "labels": ['0-2 Years', '2-5 Years', '5-10 Years', '> 10 years'],
                        }],
                    'layout': {
                        'font': {
                            'color': 'black'
                        },
                        'title': 'Work Experience',
                    }
                },
            )
        ], className='six columns'),

        html.Div([
            dcc.Graph(
                id='gender-pie',
                figure={
                    'data': [
                        {
                            'values': calc_counts.calculate_gender_count(read_data.df_sel_col),
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
                id='age-Id',
                figure={
                    'data': [
                        {'x': ['20-30 Years', '30-40 Years', '40-50 Years', '> 50 Years'],
                         'y': calc_counts.calculate_age_counts(read_data.df_sel_col),
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
    html.Div([
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in read_data.df_sel_col.columns],
            data=read_data.df_sel_col.to_dict("rows"),
            editable=False,
            # scroll enabled
            style_table={'maxWidth': '1500px', 'overflowY': 'scroll', 'maxHeight': '400px',
                         'border': 'thin lightgrey solid'},
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
            selected_rows=[],
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
])
################################################################################################