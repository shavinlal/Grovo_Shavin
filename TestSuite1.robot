*** Settings ***

#Library           TestCases/BaseTestClass.py
#Library           TestCases/BasicInformationValidData_27.py
#Library           TestCases/BasicInformationWithDirectRole_28.py

Library           TestCases/BaseTestClass.py
Library           TestCases/TeachASkill.py
Library           TestCases/LessonExplainAConcept.py
Library           TestCases/IntroduceATopic.py
Library           TestCases/BlankLessonTwo.py
Library           TestCases/BlankLessonTen.py
Library           TestCases/BlankLessonOne.py
#Library          TestCases/BlankLessonFiveTwo.py
Library           TestCases/BlankLessonFive.py

*** Test Cases ***
TC0 - User Login
    User Login

#TC27
    #BasicInformationValidData_27.User Creation With Valid Data
    #BasicInformationValidData_27.Logincreateuser
    #BasicInformationValidData_27.Againuser Login

#TC28
    #BasicInformationWithDirectRole_28.User Creation With Direct Role
    #BasicInformationWithDirectRole_28.Logincreateuser
    #BasicInformationWithDirectRole_28.Againuser Login



#TeachASkill
    #Teach A Skill Main

#IntroduceATopic
    #Introduce A Topic Main

#LessonExplainAConcept
    #Lesson Explain A Concept Main

BlankLessonTwo
    Blank Lesson Two Main

BlankLessonTen
    Blank Lesson Ten Main

BlankLessonOne
    Blank Lesson One Main

#BlankLessonFiveTwo
   # Blank Lesson Five Two Main

BlankLessonFive
    Blank Lesson Five Main
