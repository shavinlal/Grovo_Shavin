*** Settings ***
Library   TestCases/BaseTestClass.py
Library   TestCases/CreateTagDocLesson.py
Library   TestCases/CreateTagImageLesson.py
Library   TestCases/CreateTagLessonCombinedLesson.py
Library   TestCases/CreateTagLessonExplainAconcept.py


*** Test Cases ***
TC0 - User Login
    User Login

TC1 - CreateTagDocLesson
    Creating Tag For Document Lesson
    
TC2 - CreateTagImageLesson
    Create Tag For Image Lesson
    
TC3 - CreateTagLessonCombinedLesson
    Create Tag For Combined Lesson
    
TC4 - CreateTagLessonExplainAconcept
    Create Tag For Lesson Explain A Concept
 
