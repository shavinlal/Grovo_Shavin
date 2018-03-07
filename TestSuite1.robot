*** Settings ***

*** Config ***
Library   TestCases/BaseTestClass.py

*** Fucntions for Test Bed cleanup ***
Library   TestCases/Delete_Tags_Attributes_Lessons.py
Library   TestCases/DeleteLesson.py

*** Functions for User Creation with standard roles ***
Library   TestCases/CreateCreator.py
Library   TestCases/CreateLearner.py
Library   TestCases/CreateLearnerAdministrator.py
Library   TestCases/CreateMasterAdmin.py

*** Functions to create Lessons ***
Library   TestCases/BlankLessonOne.py
Library   TestCases/LessonExplainAConcept.py
Library   TestCases/TeachASkill.py
Library   TestCases/LessonCreateImage.py
Library   TestCases/LessonCreateVideo.py

*** Functions to create Tracks ***
Library   TestCases/TrackWithTxtImgQueLesson.py
Library   TestCases/TrackWithDocumentLesson.py
Library   TestCases/TrackWithImageLesson.py
Library   TestCases/TrackWithQuestionLesson.py


*** Test Cases ***
TC0 - User Login
    User Login
 
*** Test cases for User Creation with standard roles ***
TC9 - CreateCreator
    Create Creator User And Validation
TC10 - CreateLearner
    Create Learner User And Validation
TC11 - CreateLearnerAdministrator
    Create Learner Admin User And Validation
TC12 - CreateMasterAdmin
    Create Master Admin User And Validation

*** Test cases for Lesson creation ***
TC4 - BlankLessonOne
    Blank Lesson One Main
TC7 - LessonExplainAConcept
    Lesson Explain A Concept Main
TC8 - TeachASkill
    Teach A Skill Main
TC25 - LessonCreateImage
    Lesson With Image Upload Card
TC26 - LessonCreateVideo
    Lesson With Video Upload Card
    
*** Test cases for Track creation ***
TC34 - TrackWithTxtImgQueLesson
    Lesson With Text Image Question Card
TC30 - TrackWithDocumentLesson
    Lesson With Document Card
TC31 - TrackWithImageLesson
    Lesson With Image Card
TC32 - TrackWithQuestionLesson
    TrackWithQuestionLesson.Lesson With Question Answer Card    
