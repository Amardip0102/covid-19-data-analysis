#############################################################
# Importing all module dependencies
#############################################################
import dash_core_components as dcc
import dash_html_components as html
#############################################################
help_layout = html.Div([

    html.Div([
        html.Label(
            children='This page contains the information of how to use POST COVID 19 EVALUATION dashboard.',
            style={'textAlign': 'center', 'color': 'black', 'font-weight': 'bold'}
        ),
        dcc.Markdown('''
                                > * **Tabs on Dashboard **
                                    * _Basic Filters_
                                    * _Advanced Filters_
                                    * _Help_
                                    * _About_ 
                            ''',
                     style={'color': 'black', 'font': "16px Arial", 'font-weight': 'bold'})
    ]),

#############################################################
# Styling and information for Basic Filters
#############################################################

    html.Div([
        html.Label(
            children='\nBasic Filters on Dashboard',
            style={'color': 'black', 'font-weight': 'bold'}
        ),
        dcc.Markdown('''
            ```
            For ease of use, you can choose filter options that can give the information of the employee at your fingertips.  
            User has basic filter options as listed below and its description:  

            1. Team  
                • Specific Team  
            2. Designation  
            3. Gender  
            4. Experience  
            5. Age  
            6. Reset Filters  
            ```
            
            ###### **`Team :`** 
            `The Team filter helps user to get accurate information about the employee
            list of team and its division is as follows: 
            `   
            **`1. SupportFunctions`** 
            ```
               • HR  
               • ADMIN  
               • Sales  
               • Finance
            ``` 
            **`2. IT+ToolsAndQuality`**
            ```  
               • PMT  
               • IT  
               • Quality  
               • Instru
            ```  
            **`3. AdvanceEngineering+2W/3W`**
            ```  
               • AE-ML  
               • AE  
               • 2W/3W
            ```
            **`4. MechanicalDesign`**
            ```  
               • Mechanical-Design
            ```  
            **`5. System_Fusa`**
            ```    
               • System/FuSa
            ```    
            **`6. Software`**
            ```  
               • SW-DEV-EST  
               • SW-DEV-DIAG  
               • SW-DEV-EPS  
               • SW-DEV-GL  
               • SW-DEV-VBS  
               • SW-DEV-STAR3  
               • SW-DEV-ADAS  
               • SW-DEV-TBCM  
               • SW-DEV-RPAS  
               • SW-DEV-DCDC  
               • SW-DEV-OTHER  
            ```  
            **`7. Testing`**
            ```	  
               • TEST-AudiSAR  
               • TEST-STAR3  
               • TEST-EPS  
               • TEST-TATA  
               • TEST-BCM2Evo  
               • TEST-COBAS-VBS  
               • TEST-RPAS  
               • TEST-OTHER  
            ```  
            **`8. Hardware`**
            ```  
               • HW-LAYOUT    
               • HW-DESIGN
               • HW-OTHER       
            ```  
            **`9. Others`**
            ```  
               • OTHERS-NOT-LISTED  
            ```

            ###### **`Designation :`** 
            ``` 
            The Designation filter helps the user to segregate the employee based on their designation.  
            List of designations is as follows:  

            • Engineer  
            • Sr. Engineer  
            • Specialist  
            • Sr. Specialist  
            • Tech/Team Lead  
            • Dy. Manager  
            • Manager  
            • Assistant Manager  
            • Sr. Manager  
            • Dy. Architect  
            • Architect  
            • Sr. Architect  
            • Dy. General Manager  
            • General Manager  
            • Other  
            ```

            ###### **`Gender :`**
            ```
            The Gender filter helps the user to segregate the employee based on their gender which is as follows:
            • Male 
            • Female  
            • Others        
            ```

            ###### **`Experience :`**
            ```
            The Experience filter helps the user to segregate the employee based on their work experience(In Years) which is as follows:
            • 0-2  Years  
            • 2-5  Years  
            • 5-10 Years
            • >10  Years  
            ```

            ###### **`Age :`**
            ```
            The Age filter helps the user to segregate the employee based on their age(In Years) which is as follows:
            • 20-30 Years  
            • 30-40 Years  
            • 40-50 Years
            • >50   Years  
            ```

            ###### **`Reset Button :`**
            ```
            The Reset button option provides the user to reset all filters to default selection which is “All” i.e. no segregation,  
            data of all the employees are shown on the charts and graphs.
            ```
            
            ###### **`Data processed using this filter: `**
            ```
            This is the count of employee data which is processed as per the basic filter selected by the user.  
            By default, this shows the count of all the employee data.  
            ```
            
            ###### **`Based on the basic filters selection, user can see charts and graphs of the data of employees`**  
            ```
            ```
            ###### **`Display Data: `**
            ```
            Display data provides the data of all the employees as per selected filter.  
            In Display data, left-top side there is a button called "EXPORT" which can directly save your data in to XLSX.  
            ```
            ```
            
        ''',
                     style={"border": "1px black solid", 'color': 'black'}, className="row"),
    ]),

#############################################################
# Styling and information for Advanced Filters
#############################################################

    html.Div([
        html.Label(
            children='\nAdvanced Filters on Dashboard',
            style={'color': 'black', 'font-weight': 'bold'}
        ),
        dcc.Markdown('''
                    ```  
                    The tool provides some advanced filters that will help the user to process the data to a great extent.  
                    The advanced filters are listed below :   

                    1. Travel risk severity 
                    2. Office to home Travel distance 
                    3. Health Condition Severity 
                    4. Exposure Severity to affected areas 
                    5. Contact with covid19 severity 
                    6. Living with Number of people
                    7. Sr Citizen / Kids 
                    8. Mode of Transportation to office 
                    ```                             

                    ###### **`Travel risk severity :`**   
                    ```
                    This filter helps the user to segregate the employee as per the risk the employee will have if need to reach his/her workplace.  
                    The filtering options are as follows:  
                    • All   
                    • Low   
                    • Medium   
                    • High   
                    ```
                    
                    ###### **`Office to home Travel distance :`**  
                    ```
                    This filter helps the user to segregate the employee as per the distance employee need to travel to reach his/her workplace.  
                    The filtering options are as follows:  
                    • All  
                    • 0 – 5 Kms   
                    • 6 – 10 Kms  
                    • 11- 15 Kms   
                    • 16 – 20 Kms   
                    • > 20 Kms    
                    ```

                    ###### **`Health Condition Severity :`**  
                    ```
                    This filter helps the user to segregates the employee as per their health conditions.  
                    The filtering options are as follows:  
                    • All   
                    • Low   
                    • Medium   
                    • High   
                    ```

                    ###### **`Exposure Severity to affected areas :`**  
                    ```
                    This filter helps the user to segregates the employee who may have a different levels of exposure to the hotspots for COVID19.   
                    The filtering options are as follows:  
                    • All   
                    • Low   
                    • Medium   
                    • High   
                    ```

                    ###### **`Contact with covid19 severity  :`**  
                    ```
                    This filter helps the user to segregate the employee with the risk of contact with COVID19 positive patients.  
                    The filtering options are as follows:  
                    • All   
                    • Low   
                    • Medium   
                    • High                       
                    ```

                    ###### **`Living with Number of people :`**  
                    ```
                    This filter helps the user to segregate the employee with a number of the person he/she stays with.  
                    The filtering options are as follows:  
                    • 0 - 5 persons   
                    • 5 - 10 persons   
                    • > 10 persons  
                    ```
                    
                    ###### **`Sr Citizen / Kids :`**   
                    ```
                    This filter helps the user to segregate the employee who stays with a kid(<5 years) or with a senior citizen.    
                    The filtering options are as follows:  
                    • Yes     
                    • No   
                    ```
                    
                    ###### **`Mode of Transportation to office :`**   
                    ```
                    This filter helps the user to segregate the employee on the basis of which transportation they are going to use after lockdown to reach the office.      
                    The filtering options are as follows:  
                    • 2 Wheeler       
                    • 4 Wheeler  
                    • Shared Car  
                    • Public Transport
                    • By Walk     
                    ```
                    
                    ###### **`Reset Button :`**
                    ```
                    The Reset button option provides the user to reset all filters to default selection which is “All” i.e. no segregation,  
                    data of all the employees are shown on the charts and graphs.
                    ```
                    
                    ###### **`Data processed using Basic+Advanced : `**
                    ```
                    This is the count of employee data which is processed as per the advance filter selected by the user.  
                    By default, this shows the count of all the employee data.  
                    ```
                    
                    ###### **`Based on the basic + advanced filters selection, user can see charts and graphs of the data of employees`**  
                    ```
                    
                    ```
                    ###### **`Display Data: `**  
                    ```
                    Display data provides the data of all the employees as per selected filter.  
                    In Display data, left-top side there is a button called "EXPORT" which can directly save your data in to XLSX.  
                    ```
                    ```
                ''', style={"border": "1px black solid"}, className="row")
    ]),

#############################################################
# Styling and information for Help
#############################################################

    html.Div([
        html.Label(
            id='Help',
            children='\nHelp',
            style={'color': 'black', 'font-weight': 'bold'}
        ),
        dcc.Markdown('''
            ```
            This tab helps the user to understand the tool and how to use the options effectively to get the employee information.  

            ```
            ''', style={"border": "1px black solid"}, className="row"),
    ]),

#############################################################
# Styling and information for About
#############################################################

    html.Div([
        html.Label(
            children='\nAbout',
            style={'color': 'black', 'font-weight': 'bold'}
        ),
        dcc.Markdown('''
            ```
            This tab gives information about the tool which includes details like the version of the tool, contact information, copyrights, etc.  

            ```
            ''', style={"border": "1px black solid"}, className="row"),
    ]),
])
