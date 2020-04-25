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
                    'color': 'black',
                    'font': "18px Arial",
                }
            ),

            dcc.Markdown(
                '''
                > * **SW VERSION** - _HIA-ADAS-COVID-19-Beta-1.2_
                > * **Contact:**
                    *   Amardip Ghodichor  (Amardip.Ghodichor@hella.com)
                    *   Mahammadajar Awati (Mahammadajar.Awati@hella.com)
                    *   Swapnil Balpande   (swapnil.balpnade@external.hella.com)
                    *   Keyur Joshi        (Keyur.Joshi@hella.com)
                    *   Ammolh Kulkarni    (Ammolh.Kulkarni@hella.com)
                    )
                > * **Support:**
                    *  _HIA-ADAS-TEAM_
                ''',
                style={
                    'textAlign': 'left',
                    'color': 'black',
                    'font': "18px Arial",
                }
            )

        ],style={"border": "2px blue solid"}, className="row")
])