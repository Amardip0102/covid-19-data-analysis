def fetchFilteringData():
    teamsList = {
                'All' : ['All'],
                'SupportFunctions': ['HR','ADMIN','SALES','FINANCE'],
                'IT+ToolsAndQuality': ['PMT','IT','QUALITY','INSTRU'],
                'advanceEngineering+2W/3W': ['AE-ML','AE','2W/3W'],
                'MechanicalDesign': ['MechanicalDesign'],
                'System_Fusa': ['System_Fusa'],
                'software': ['SW-DEV-EST','SW-DEV-DIAG','SW-DEV-EPS','SW-DEV-GL','SW-DEV-VBS','SW-DEV-STAR3','SW-DEV-ADAS',
                              'SW-DEV-TBCM','SW-DEV-RPAS','SW-DEV-DCDC','SW-DEV-OTHER'],
                'SystemTesting': ['SYS_TEST-AudiSAR','SYS_TEST-STAR3','SYS_TEST-EPS','SYS_TEST-TATA','SYS_TEST-BCM2Evo',
                                  'SYS_TEST-COBAS-VBS','SYS_TEST-RPAS','SYS-TEST-OTHER'],
                'hardware': ['HW-LAYOUT-LIBRARY','HW-DESIGN','HW-RADIO-HOMOLOGATION','HW-OTHER'],
                'others': ['OTHERS-NOT-LISTED']
                }

    designations = ['All', 'Engineer', 'Sr. Engineer', 'Specialist', 'Sr. Specialist', 'Tech-Team Lead', 'Dy. Manager', 'Manager',
                    'Assistant Manager', 'Sr. Manager', 'Dy. Architect', 'Architect', 'Sr. Architect',
                    'Dy. General Manager', 'General Manager', 'Other']


    experience = ['All','0-2 Years', '2-5 Years', '5-10 Years', '> 10 Years']

    age = ['All', '20-30 Years', '30-40 Years', '40-50 Years', '> 50 Years']

    gender = ['All', 'Male', 'Female', 'Other']
    return teamsList, designations, experience, age, gender
