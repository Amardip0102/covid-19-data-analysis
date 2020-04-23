#############################################################
# DATASET FOR ALL FILTERS SAME AS FORM
#############################################################
teamsList = {
            'All' : ['All'],
            'SupportFunctions': ['HR','ADMIN','SALES','FINANCE'],
            'IT+ToolsAndQuality': ['PMT','IT','QUALITY','INSTRU'],
            'advanceEngineering+2W/3W': ['AE-ML','AE','2W/3W'],
            'MechanicalDesign': ['MECHANICAL-DESIGN'],
            'System_Fusa': ['SYSTEM/FuSa'],
            'Software': ['SW-DEV-EST','SW-DEV-DIAG','SW-DEV-EPS','SW-DEV-GL','SW-DEV-VBS','SW-DEV-STAR3','SW-DEV-ADAS',
                          'SW-DEV-TBCM','SW-DEV-RPAS','SW-DEV-DCDC','SW-DEV-OTHER'],
            'SystemTesting': ['SYS_TEST-AudiSAR','SYS_TEST-STAR3','SYS_TEST-EPS','SYS_TEST-TATA','SYS_TEST-BCM2Evo',
                              'SYS_TEST-COBAS-VBS','SYS_TEST-RPAS','SYS-TEST-OTHER'],
            'Hardware': ['HW-LAYOUT-LIBRARY','HW-DESIGN','HW-RADIO-HOMOLOGATION','HW-OTHER'],
            'Others': ['OTHERS-NOT-LISTED']
            }

designations = ['All', 'Engineer', 'Sr. Engineer', 'Specialist', 'Sr. Specialist', 'Tech/Team Lead', 'Dy. Manager', 'Manager',
                'Assistant Manager', 'Sr. Manager', 'Dy. Architect', 'Architect', 'Sr. Architect',
                'Dy. General Manager', 'General Manager', 'Other']


experience = {'All': 'All','0-2 Years': '0 - 2', '2-5 Years': '2 - 5', '5-10 Years':'5 - 10', '> 10 Years': '> 10'}

age = {'All': 'All', '20-30 Years': '20 - 30', '30-40 Years': '30 - 40', '40-50 Years': '40 - 50', '> 50 Years': '> 50'}

gender = ['All', 'Male', 'Female', 'Other']

distance = {'All' :'All', '0-5 Kms':'0 - 5', '6-10 kms':'6 - 10', '10-15 Kms':'10 - 15','15-20 Kms': '15 - 20',
            '>20 Kms':'> 20'}

personcount= {'All' :'All', '0-5 persons':'0 - 5', '5-10 persons':'5 - 10', '> 10 persons':'> 10'}

severity = ['All', 'Low', 'Medium', 'High']
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