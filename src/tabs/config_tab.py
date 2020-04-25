import dash
import dash_html_components as html
import dash_table
import pandas as pd
from collections import OrderedDict
import dash_core_components as dcc

df = pd.DataFrame(OrderedDict([
    ('visted_hospitals',['Yes', 'Yes', 'No','No']),
    ('visted_hotspots',['Yes', 'No', 'Yes','No']),
    ('redzone_severity', ['High', 'Medium', 'Medium','Low'])
]))

df_covidexposure = pd.DataFrame(OrderedDict([
    ('contact_covid19_patient',['Yes','No','No','No','No']),
    ('contact_travel_history',['X','Yes', 'Yes', 'No','No']),
    ('family_member_healthcare',['X','Yes','No','Yes','No']),
    ('covid_exposure_severity', ['High','High', 'Medium', 'Medium','Low'])
]))


df_travel=  pd.DataFrame(OrderedDict([
    ('travelled',['Yes','Yes','Yes','Yes','Yes','No']),
    ('still_there',['Yes','No','No','No','No','X']),
    ('when_came',['X','<14','<14','<14','<14','X']),
    ('transport',['X','Public','Private','Public','Private','X']),
    ('travel_severity',['High','High', 'Medium', 'Medium','Low','Low'])
]))


config_layout = html.Div([

    dcc.Store(id='shared-temporary-data', data=[]),
############################################################################################
    html.Div([
        html.H4(children='Redzone exposure severity',
                style={
                    'textAlign': 'left',
                    'color': 'blue',
                    'font-weight': 'bold'
                })
    ], className='row'),
    html.Div([
        dash_table.DataTable(
            id='affected_areas_exposure',
            data=df.to_dict('records'),
            columns=[
                {'id': 'visted_hospitals', 'name': 'visited hospitals'},
                {'id': 'visted_hotspots', 'name': 'visted/stayed hotspots'},
                {'id': 'redzone_severity', 'name': 'Severities', 'presentation': 'dropdown'},
            ],

            editable=True,
            dropdown={
                'redzone_severity': {
                    'options': [
                        {'label': i, 'value': i}
                        for i in df['redzone_severity'].unique()
                    ]
                }
            }
        ),

    ], style={"border": "2px black solid"}, className="row"),
##################################################################################################
 ################################################################################################
    html.Div([
        html.H4(children='Covid19 exposure severities',
                style={
                    'textAlign': 'left',
                    'color': 'blue',
                    'font-weight': 'bold'
                })
    ], className='row'),
    html.Div([
        dash_table.DataTable(
            id='contact_covid',
            data=df_covidexposure.to_dict('records'),
            columns=[
                {'id': 'contact_covid19_patient', 'name': 'contact with covid19 patient'},
                {'id': 'contact_travel_history', 'name': 'visted/stayed hotspots'},
                {'id': 'family_member_healthcare', 'name': 'family member  at healthcare'},
                {'id': 'covid_exposure_severity', 'name': 'Severities', 'presentation': 'dropdown'},
            ],

            editable=True,
            dropdown={
                'covid_exposure_severity': {
                    'options': [
                        {'label': i, 'value': i}
                        for i in df_covidexposure['covid_exposure_severity'].unique()
                    ]
                }
            }
        ),

    ], style={"border": "2px black solid"}, className="row"),
#######################################################################################################
#######################################################################################################
    html.Div([
        html.H4(children='Travel exposure severity',
                style={
                    'textAlign': 'left',
                    'color': 'blue',
                    'font-weight': 'bold'
                })
    ], className='row'),
    html.Div([
        dash_table.DataTable(
            id='travel_exposure_severity',
            data=df_travel.to_dict('records'),
            columns=[
                {'id': 'travelled', 'name': 'Travelled'},
                {'id': 'still_there', 'name': 'Still there'},
                {'id': 'when_came', 'name': ' When came in days '},
                {'id': 'transport', 'name': 'Transport Mode'},
                {'id': 'travel_severity', 'name': 'Severities', 'presentation': 'dropdown'},
            ],

            editable=True,
            dropdown={
                'travel_severity': {
                    'options': [
                        {'label': i, 'value': i}
                        for i in df_travel['travel_severity'].unique()
                    ]
                }
            }
        ),

    ], style={"border": "2px black solid"}, className="row"),
###########################################################################################################
    html.Div([
        html.Div([
            html.Label(
                'Submit to apply changes',
                style={'color': 'blue', 'font-weight': 'bold'}
            ),
            html.Button(
                'submit',
                style={'color': 'black', 'font-weight': 'bold', 'width': '30%', 'display': 'table-cell'},
                id='config-button',
                type='submit',
                n_clicks=0
            ),
        ], className="four columns"),
      ], className="row"),
   html.Div(id='table-dropdown-container'),

])