*** Settings ***
Library   TestCases/BaseTestClass.py
Library   TestCases/BasicInformationValidData_27.py
Library   TestCases/BasicInformationWithDirectRole_28.py
Library   TestCases/BasicInfoWithMultipleRoles_33.py
Library   TestCases/BasicInfoPasswordCreation_35.py
Library   TestCases/BasicInfoWithDifferentDataType_45.py


*** Test Cases ***
TC0 - User Login
      User Login
 
TC1 - BasicInformationValidData_27 
      Basic Information Valid Data
    
TC2 - BasicInformationWithDirectRole_28
      Basic Information With Direct Role 
      
TC2 - BasicInfoWithMultipleRoles_33
      Basic Information Multiple Roles      

TC2 - BasicInfoPasswordCreation_35
      Basic Information With DirectRole
      
TC2 - BasicInfoWithDifferentDataType_45
      Basic Information Valid Data
      
   
      
