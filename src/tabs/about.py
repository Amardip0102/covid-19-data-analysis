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

about_layout = html.Div([
        html.Div([
            html.H3(children='COVID-19 DATA ANALYSIS TOOL',
                    style={
                        'textAlign': 'center',
                        'color': 'black',
                        'font-weight': 'bold'
                    },
                    ),

        ], style={"border": "2px blue solid"}, className="row"),

        html.Div([
            dcc.Markdown('''
            Tool **COVID-19-DATA-ANALYSIS** is made in the interest of **HELLA India Automotive Pvt. Ltd, Pune**
            
            This program is proprietary software belongs to **HELLA India Automotive Pvt Ltd.**

            This program is distributed in the hope that it will be useful, but **WITHOUT ANY WARRANTY**; 
            without even the implied warranty of **MAINTAINABILITY**.

            ''',
             style={
                 'textAlign': 'left',
                 'color': 'black'
             }
             ),

            dcc.Markdown(
                '''
                

                ''',
                style={
                    'textAlign': 'center',
                    'color': 'black'
                }
            ),

            dcc.Markdown(
                '''
                > * **SW VERSION** - _HIA-ADAS-COVID-19-Beta-1.2_
                > * **Contact:**
                    *   _HIA-ADAS-TEAM_
                > * **Support:**
                    *  _covidatahelp@hotmail.com_
                ''',
                style={
                    'textAlign': 'left',
                    'color': 'black'
                }
            )

        ],style={"border": "2px blue solid"}, className="row")
])