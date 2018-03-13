*** Settings ***

#Config
Library   TestCases/BaseTestClass.py

#Functions to create Lessons
#Library   TestCases/BlankLessonOne.py
#Library   TestCases/LessonExplainAConcept.py
Library   TestCases/TeachASkill.py
Library   TestCases/TeachASkill.py




*** Test Cases ***
TC0 - User Login
    User Login

#Test cases for Lesson creation
#TC2 - BlankLessonOne
    #Blank Lesson One Main
    
#TC3 - LessonExplainAConcept
    #Lesson Explain A Concept Main
    
TC4 - TeachASkill
    Teach A Skill Main
TC4 - TeachASkill
    Teach A Skill Main




