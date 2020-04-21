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

advance_layout =html.Div([

   html.Div([
        ##############################################################
        # First Four Columns
        ##############################################################

        html.Div(
            [
                html.Label(
                    children='Traveled Out of Pune',
                    style={'color': 'black', 'font-weight': 'bold'}
                ),
                dcc.Dropdown(
                    id='traveled-history-dropdown',
                    options=[
                        {'label': 'All', 'value': 'All'},
                        {'label': 'Yes', 'value': 'Yes'},
                        {'label': 'No', 'value': 'No'}
                    ],
                    value= 'All'
                ),

                html.Label(
                    'Returned to Pune',
                    style={'color': 'black', 'font-weight': 'bold'}
                ),
                dcc.Dropdown
                    (
                    id='returned-travelers-dropdown',
                    options=[
                       {'label': 'All', 'value': 'All'},
                        {'label': 'Yes', 'value': 'Yes'},
                        {'label': 'No', 'value': 'No'}
                    ],
                    value= 'All',
                    disabled= True
                )
            ], className="four columns"),

        #####################################################################
        #   Four Columns
        ##############################################################
        html.Div([
            html.Label(
                'office to home distance',
                style={'color': 'black', 'font-weight': 'bold'}
            ),
            dcc.Dropdown(
                id='distance-dropdown',
                options=[{'label': k, 'value': k} for k in filtering.distance],
                value='All',
                multi=False
            ),

            html.Label(
                'Severity',
                style={'color': 'black', 'font-weight': 'bold'}
            ),
            dcc.Dropdown(
                id='severity-dropdown',
                options=[{'label': k, 'value': k} for k in filtering.severity],
                value='All',
                multi=False
            )
        ], className="four columns"),
        ##############################################################
        html.Div(
            [
                html.Label(
                    children='COVID-19 Tested',
                    style={'color': 'black', 'font-weight': 'bold'}
                ),
                dcc.Dropdown(
                    id='covid19-dropdown',
                    options=[
                        {'label': 'All', 'value': 'All'},
                        {'label': 'Yes', 'value': 'Yes'},
                        {'label': 'No', 'value': 'No'}
                    ],
                    value = 'All'
                ),

                html.Label(
                    'COVID19-Result',
                    style={'color': 'black', 'font-weight': 'bold'}
                ),
                dcc.Dropdown
                    (
                    id='covid19-result-dropdown',
                    options=[
                        {'label': 'All', 'value': 'All'},
                        {'label': 'Yes', 'value': 'Yes'},
                        {'label': 'No', 'value': 'No'}
                    ],
                     value = 'All',
                    disabled= True
                )
            ], className="four columns"),
        ##############################################################

        # end : Advanced filters here
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

    ], style={"border": "2px black solid"}, className="row"),

    # plotting graphs from here onwards
    html.Div([

    html.Div([
        dcc.Graph(
            id='work-distance',
            figure={
                'data': [
                    {
                        'values': calc_counts.calcWork_home_distance('All'),
                        'type': 'pie',
                        'name': 'Work-home-distance',
                        "labels": ['0-5 Km', '5-10 kms', '10-20 kms', '> 20 Kms'],
                    }],
                'layout': {
                    'font': {
                        'color': 'black'
                    },
                    'title': 'Work-home-distance',
                }
            },
        )
    ], className='six columns'),

        html.Div([
            dcc.Graph(
                id='travel-pie',
                figure={
                    'data': [
                        {
                            'values': calc_counts.calculate_Travel_count('All'),
                            'type': 'pie',
                            'name': 'Travel history',
                            "labels": ['Travelled', 'Not-Travelled'],
                        }],
                    'layout': {
                        'font': {
                            'color': 'black'
                        },
                        'title': 'Travel history Distribution',
                    }
                },
            )
        ], className='six columns'),

     ], style={"border": "2px black solid"}, className="row"),

  ]
)