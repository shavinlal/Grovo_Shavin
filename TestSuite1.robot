*** Settings ***
Library   TestCases/BaseTestClass.py
Library   TestCases/CreateCreator.py
Library   TestCases/CreateLearner.py
Library   TestCases/CreateLearnerAdministrator.py
Library   TestCases/CreateMasterAdmin.py


*** Test Cases ***
TC0 - User Login
    User Login

TC1 - CreateCreator
    Create Creator User And Validation

TC2 - CreateLearner
    Create Learner User And Validation

TC3 - CreateLearnerAdministrator
    Create Learner Admin User And Validation
    
TC4 - CreateMasterAdmin
    Create Master Admin User And Validation