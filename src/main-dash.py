# ----------------------------------------
# Post-COVID 19 dashboards for
#
#
# -----------------------------------------

# Importing all module dependencies
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import appLayout

# Read here your excelsheet

# data = pd.read_excel('responses.xls')

# create application instance
app = dash.Dash()

# create application layout here
'''
app.layout = html.Div([
    html.H1(children ='POST COVID 19 DASHBOARD RESULT',
            style={
                'textAlign': 'center',
                'color': '#ff0000'
            }
            ),
    html.Div(children = 'This is report for HELLA India Automotive Pvt. Ltd',
             style={
                 'textAlign': 'center',
                 'color': '#0000ff'
             }
             ),


    dcc.Graph(
        id = 'some-Graph',
        figure = {
            'data' : [
                {'x':[1,2,5], 'y':[4,8,12], 'type': 'bar', 'name': 'simpleGraph'},
                {'x':[1,2,5], 'y':[10,9,15], 'type': 'bar', 'name': 'newSimpleGraph'},
            ],
            'layout': {
                # experiment and finalise colors
                # 'plot_bgcolor': '#90EE90',
                # 'paper_bgcolor': '#90EE90',
                'font' : {
                    'color' : '#ff0000'
                },
                'title': 'First Chart'
            }
        }
    )
])
'''

app.layout = html.Div([
    html.Label('Choose Team'),
    dcc.Dropdown(
        id = 'first-d',
        options = [
            {'label': 'EST', 'value': 'SW-DEV-EST'},
            {'label': 'DIAG', 'value': 'SW-DEV-DIAG'},
            {'label': 'TBCM', 'value': 'SW-DEV-TBCM'} # disabled = True
        ],
        value= 'SW-DEV-EST', #default
        placeholder= 'select a team',
        # disabled= True
        multi = True
    ),
    html.Label('AGE SLIDER'),
    dcc.Slider(
        min = 20,
        max = 60,
        value = 5,
        step = 1,
        marks = {i:i for i in range(20,60)}
    )
])

# start our main application
if __name__ == '__main__':
    app.run_server(port = 4050)