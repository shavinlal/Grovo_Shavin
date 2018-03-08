*** Settings ***

#Config
Library   TestCases/BaseTestClass.py
#Functions for User Creation with standard roles
Library   TestCases/CreateCreator.py
Library   TestCases/CreateLearner.py
Library   TestCases/CreateLearnerAdministrator.py
Library   TestCases/CreateMasterAdmin.py


*** Test Cases ***
TC0 - User Login
    User Login

#Test cases for User Creation with standard roles
TC29 - CreateCreator
    Create Creator User And Validation
    
TC30 - CreateLearner
    Create Learner User And Validation
    
TC31 - CreateLearnerAdministrator
    Create Learner Admin User And Validation
    
TC32 - CreateMasterAdmin
    Create Master Admin User And Validation
