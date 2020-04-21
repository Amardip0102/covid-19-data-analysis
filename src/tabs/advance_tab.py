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
                    children='Travel risk severity',
                    style={'color': 'black', 'font-weight': 'bold'}
                ),
                dcc.Dropdown(
                    id='travel_risk_severity',
                    options=[{'label': k, 'value': k} for k in filtering.severity],
                    value= 'All'
                ),

                html.Label(
                    'Exposure Severity to affected areas ',
                    style={'color': 'black', 'font-weight': 'bold'}
                ),
                dcc.Dropdown
                    (
                    id='exposure_affected_severity',
                    options=[{'label': k, 'value': k} for k in filtering.severity],
                    value= 'All'
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
                options=[{'label': k, 'value': k} for k in filtering.distance],
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
                    id='health_risk_severity',options=[{'label': k, 'value': k} for k in filtering.severity],
                    value = 'All'
                ),

                html.Label(
                    'Living with Number of people',
                    style={'color': 'black', 'font-weight': 'bold'}
                ),
                dcc.Dropdown
                    (
                    id='people-living-count',
                    options=[{'label': k, 'value': k} for k in filtering.personcount],
                    value='All'

                )
            ], className="four columns"),
        ##############################################################

        # end : Advanced filters here
        #############################################################

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