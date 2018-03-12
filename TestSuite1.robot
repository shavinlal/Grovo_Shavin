*** Settings ***

#Config
Library   TestCases/BaseTestClass.py

#Fucntions for Test Bed cleanup
Library   TestCases/Delete_Tags_Attributes_Lessons.py
#Library   TestCases/DeactivateUser.py
#Library   TestCases/UpdatingUserDetails.py

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
Library   TestCases/CampaignPageDisplay.py

#Functions for User Creation with standard roles
Library   TestCases/CreateCreator.py
Library   TestCases/CreateLearner.py
Library   TestCases/CreateLearnerAdministrator.py
Library   TestCases/CreateMasterAdmin.py


*** Test Cases ***
TC0 - User Login
    User Login
    
TC1 - Delete_Tags_Attributes_Lessons
    Main Delete All
  
#TC - DeactivateUser
 #   Created User Deactivation

#TC - UpdatingUserDetails
 #   Updation Of Excel Values
    
#Test cases for Lesson creation
TC2 - BlankLessonOne
    Blank Lesson One Main
    
TC3 - LessonExplainAConcept
    Lesson Explain A Concept Main
    
TC4 - TeachASkill
    Teach A Skill Main
TC5 - LessonCreateImage
    Lesson With Image Upload Card
TC6 - LessonCreateVideo
    Lesson With Video Upload Card
    
#Test cases for Track creation
TC7 - TrackWithTxtImgQueLesson
    Lesson With Text Image Question Card
    
TC8 - TrackWithDocumentLesson
    Lesson With Document Card
    
TC9 - TrackWithImageLesson
    Lesson With Image Card
    
TC10 - TrackWithQuestionLesson
    TrackWithQuestionLesson.Lesson With Question Answer Card   



#Test cases for Campaign creation   
TC11 - CreateCampaignForTextLesson
    Create Campaign Text Lesson

TC12 - CreateCampaignForImageLesson
    Create Campaign Image Lesson

TC13 - CreateCampaignForVideoLesson
    Create Campaign Video Lesson

TC14 - CreateCampaignForDocumentLesson
    Create Campaign Document Lesson

TC15 - CreateCampaignForQuestionLesson
    Create Campaign Question Lesson

TC16 - CreateCampaignForTxtImgQueLesson
    Create Campaign Text Image Ques Lesson

TC17 - CreateCampaignForAllCardsOneTime
    Create Campaign All Cards One Time Lesson

TC18 - CreateCampaignForAllCardsTwoTime
    Create Campaign With All Cards Two Time Lesson

TC19 - CreateCampaignForTxtVidQuesLesson
    Create Campaign With Lesson Text Video Question

TC20 - CreateCampaignForVidDocQueLesson
    Create Campaign With Lesson Video Document Question

#TC21 - CreateCampaignForFourLessonsOne
 #   Create Campaign With Four Lessons One

TC22 - CreateCampaignForFourLessonsTwo
    Create Campaign With Four Lessons Two

#TC23 - CreateCampaignForFourLessonsThree
   # Create Campaign With Four Lessons Three

TC24 - CreateCampaignForTextAndImageLesson
    Create Campaign With Text Lesson Image Lesson

TC25 - CreateCampaignForImageAndVideoLesson
    Create Campaign With Image Lesson Video Lesson

#TC26 - CreateCampaignForQuesLesssonAllCards1timeAllCards2TimeLessons
 #   Create Campaign With Three Lessons

TC27 - CreateCampaignForVideoLsnDocLsQuestionLes
    Create Campaign With Video Lesson Document Lesson Question Lesson  
   
#TC28 - CampaignPageDisplay
 #   Campaigns Page Display Main


#Test cases for User Creation with standard roles
#TC29 - CreateCreator
 #   Create Creator User And Validation
    
#TC30 - CreateLearner
 #   Create Learner User And Validation
    
#TC31 - CreateLearnerAdministrator
 #   Create Learner Admin User And Validation
    
#TC32 - CreateMasterAdmin
 #   Create Master Admin User And Validation 
