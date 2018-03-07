*** Settings ***

#Config
Library   TestCases/BaseTestClass.py

#Fucntions for Test Bed cleanup
Library   TestCases/Delete_Tags_Attributes_Lessons.py

#Functions to create Lessons
Library   TestCases/BlankLessonOne.py
Library   TestCases/LessonExplainAConcept.py
Library   TestCases/TeachASkill.py
Library   TestCases/LessonCreateImage.py
Library   TestCases/LessonCreateVideo.py

#Functions to create Tracks
Library   TestCases/TrackWithTxtImgQueLesson.py
Library   TestCases/TrackWithDocumentLesson.py
Library   TestCases/TrackWithImageLesson.py
Library   TestCases/TrackWithQuestionLesson.py

#Functions to create Campaign
Library   TestCases/CampaignPageElements.CampPage
Library   TestCases/CreateCampaignForTextLesson.py
Library   TestCases/CreateCampaignForImageLesson.py
Library   TestCases/CreateCampaignForVideoLesson.py
Library   TestCases/CreateCampaignForDocumentLesson.py
Library   TestCases/CreateCampaignForQuestionLesson.py
Library   TestCases/CreateCampaignForAllCardsOneTime.py
Library   TestCases/CreateCampaignForTxtImgQueLesson.py
Library   TestCases/CreateCampaignForAllCardsTwoTime.py
Library   TestCases/CreateCampaignForTxtVidQuesLesson.py
Library   TestCases/CreateCampaignForVidDocQueLesson.py
Library   TestCases/CreateCampaignForFourLessonsOne.py
Library   TestCases/CreateCampaignForFourLessonsTwo.py
Library   TestCases/CreateCampaignForFourLessonsThree.py
Library   TestCases/CreateCampaignForTextAndImageLesson.py
Library   TestCases/CreateCampaignForImageAndVideoLesson.py
Library   TestCases/CreateCampaignForQuesLesssonAllCards1timeAllCards2TimeLessons.py
Library   TestCases/CreateCampaignForVideoLsnDocLsQuestionLes.py


*** Test Cases ***
TC0 - User Login
    User Login
    
TC1 - Delete_Tags_Attributes_Lessons
    Main Delete All

#Test cases for Lesson creation
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
    
#Test cases for Track creation
TC34 - TrackWithTxtImgQueLesson
    Lesson With Text Image Question Card
TC30 - TrackWithDocumentLesson
    Lesson With Document Card
TC31 - TrackWithImageLesson
    Lesson With Image Card
TC32 - TrackWithQuestionLesson
    TrackWithQuestionLesson.Lesson With Question Answer Card   
    
TC81 - CreateCampaignForTextLesson
    Create Campaign Text Lesson

TC82 - CreateCampaignForImageLesson
    Create Campaign Image Lesson

TC83 - CreateCampaignForVideoLesson
    Create Campaign Video Lesson

TC84 - CreateCampaignForDocumentLesson
    Create Campaign Document Lesson

TC85 - CreateCampaignForQuestionLesson
    Create Campaign Question Lesson

TC86 - CreateCampaignForTxtImgQueLesson
    Create Campaign Text Image Ques Lesson

TC87 - CreateCampaignForAllCardsOneTime
    Create Campaign All Cards One Time Lesson

TC88 - CreateCampaignForAllCardsTwoTime
    Create Campaign With All Cards Two Time Lesson

TC89 - CreateCampaignForTxtVidQuesLesson
    Create Campaign With Lesson Text Video Question

TC90 - CreateCampaignForVidDocQueLesson
    Create Campaign With Lesson Video Document Question

TC91 - CreateCampaignForFourLessonsOne
    Create Campaign With Four Lessons One

TC92 - CreateCampaignForFourLessonsTwo
    Create Campaign With Four Lessons Two

TC93 - CreateCampaignForFourLessonsThree
    Create Campaign With Four Lessons Three

TC94 - CreateCampaignForTextAndImageLesson
    Create Campaign With Text Lesson Image Lesson

TC95 - CreateCampaignForImageAndVideoLesson
    Create Campaign With Image Lesson Video Lesson

TC96 - CreateCampaignForQuesLesssonAllCards1timeAllCards2TimeLessons
    Create Campaign With Three Lessons

TC97 - CreateCampaignForVideoLsnDocLsQuestionLes
    Create Campaign With Video Lesson Document Lesson Question Lesson    
