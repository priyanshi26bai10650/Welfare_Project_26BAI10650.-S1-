# INCLUSION WELFARE SYSTEM
1. Overview of the Project
The Inclusion Welfare System is a Python command line application developed to manage citizens’ basic information and their eligibility for welfare schemes. Users enter information about each citizen ( Name, Age, Annual Income, Disability and Student Status) when registering them in the application. Once entered, the application will check the citizen’s eligibility for welfare schemes based upon the eligibility criteria within the application. After evaluating the citizen’s eligibility, the application will display to the user the welfare schemes that the citizen is eligible for.
In addition to displaying welfare schemes that the citizen is eligible for, the application will store all citizen’s information in a JSON file. This allows for easy access to the citizen’s information should the user wish to use it later.

2. Features 
The following are the main features of the application: 
 - Register new citizen
 - Validate the age and income inputs 
 - Accept a yes/no response for disability information 
 - Accept a yes/no response for student status
 - Automatically check eligibility for welfare schemes 
 - Assign multiple welfare schemes to a single citizen when appropriate 
 - Save the citizen records in a JSON file  
 - View all registered citizens 
 - Generate a welfare analytics report 
 - Test the eligibility criteria automatically

 3. Technologies/tools Used 
    The technologies used in developing the application are:  Python 3 , JSON , Git , GitHub  , Visual Studio Code. 

4. Steps to install & run the project
    
    Step 1: Install Python 3
    Step 2: Check Python with python --version
    Step 3: Clone the GitHub repository
    Step 4: Enter the project folder using cd
    Step 5: Run python main.py
    Step 6: Select one of the five menu options
    Start the application using the command : python main.py
    After starting the program, the following options are displayed:
       - Add citizen : Register and save a new citizen's information.
       - Check welfare schemes : Select a citizen and check the welfare schemes they are eligible for.
       - Show all citizens : Show all stored citizen records.
       - Show report : Show the welfare report.
       - Exit : Close the application.

 5. Instructions for testing
   To Test the program, run : python test_system.py
  