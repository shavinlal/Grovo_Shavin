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
Library   TestCases/CampPage
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
    

TC30 - TrackWithDocumentLesson
    Lesson With Document Card
