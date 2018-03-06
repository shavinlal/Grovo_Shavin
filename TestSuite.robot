
*** Settings ***
Library   TestCases/BaseTestClass.py

Library   TestCases/BlankLessonFive.py
Library   TestCases/BlankLessonFiveTwo.py
Library   TestCases/BlankLessonOne.py
Library   TestCases/BlankLessonTen.py
Library   TestCases/BlankLessonTwo.py
Library   TestCases/LessonExplainAConcept.py
Library   TestCases/TeachASkill.py


Library   TestCases/CreateCreator.py
Library   TestCases/CreateLearner.py
Library   TestCases/CreateLearnerAdministrator.py
Library   TestCases/CreateMasterAdmin.py
Library   TestCases/CreateTagDocLesson.py
Library   TestCases/CreateTagImageLesson.py
Library   TestCases/CreateTagLessonCombinedLesson.py
Library   TestCases/CreateTagLessonExplainAconcept.py
Library   TestCases/CreateTagLessonIntroduceAtopic.py
Library   TestCases/CreateTagLessonLimitedmultiplecardlesson_1.py
Library   TestCases/CreateTagLessonLimitedmultiplecardlesson_2.py
Library   TestCases/CreateTagLessonLimitedmultiplecardlesson_3.py
Library   TestCases/CreateTagLessonMultiplecardlesson.py
Library   TestCases/CreateTagLessonPowerpoint.py
Library   TestCases/CreateTagLessonScorm.py
Library   TestCases/CreateTagLessonTeachAskill.py
Library   TestCases/CreateTagLessonTextLesson.py
Library   TestCases/CreateTagQuesLesson.py
Library   TestCases/CreateTagTrackLessonDocument.py
Library   TestCases/CreateTagTrackLessonFiveVideoDocumentQuestion.py
Library   TestCases/CreateTagTrackLessonImage.py
Library   TestCases/CreateTagTrackLessonOneTextImageVideoDocumentQuestion.py
Library   TestCases/CreateTagTrackLessonQuestion.py
Library   TestCases/CreateTagTrackLessonTenTextVideoQuestion.py
Library   TestCases/CreateTagTrackLessonTwoTextImageVideoDocumentQuestion.py
Library   TestCases/CreateTagTrackLessonVideo.py
Library   TestCases/CreateTagTrackWithTwolessons_1_2.py
Library   TestCases/CreateTagTrackWithTwolessons_2_3.py
Library   TestCases/CreateTagTrackWithfourlessons10_12_3.py
Library   TestCases/CreateTagTrackWithfourlessons4_5_6_7.py
Library   TestCases/CreateTagTrackWithfourlessons78910.py
Library   TestCases/CreateTagTrackWithonelesson_9.py
Library   TestCases/CreateTagTrackWiththreelessons_3_4_5.py
Library   TestCases/CreateTagTrackWiththreelessons_5_6_7.py
Library   TestCases/CreateTagTracklessonFiveTextImageQuestion.py
Library   TestCases/CreateTagVideoLesson.py
Library   TestCases/UserAttributeCheckboxWithReq.py
Library   TestCases/UserAttributeWithoutCheckbox.py
Library   TestCases/UserAttributeDateWithReq.py
Library   TestCases/UserAttributeDateWithoutReq.py
Library   TestCases/UserAttributeListWithReq.py
Library   TestCases/UserAttributeListWithoutReq.py
Library   TestCases/UserAttributeNumWithReq.py
Library   TestCases/UserAttributeNumWithoutReq.py
Library   TestCases/UserAttributeTextWithReq.py
Library   TestCases/UserAttributeTextWithoutReq.py
Library   TestCases/UserAttributeUserReferenceWithReq.py
Library   TestCases/UserAttributeUserReferenceWithoutReq.py
Library   TestCases/UserAttributeWithEmail.py
Library   TestCases/UserAttributeWithoutEmail.py



Library   TestCases/LessonCreateImage.py
Library   TestCases/LessonCreateVideo.py
Library   TestCases/TrackWithDocumentLesson.py
Library   TestCases/TrackWithImageLesson.py
Library   TestCases/TrackWithQuestionLesson.py
Library   TestCases/TrackWithTextLesson.py
Library   TestCases/TrackWithTxtImgQueLesson.py
Library   TestCases/TrackWithVideoLesson.py
Library   TestCases/TrackWithVidLessonDocLesssonQuesLesson.py
Library   TestCases/LessonCreateDocument.py
Library   TestCases/LessonCreateQuestion.py
Library   TestCases/LessonCreateText.py
Library   TestCases/TrackWithImgLessonVidLesson.py
Library   TestCases/TrackWithTxtLessonImgLesson.py
Library   TestCases/TrackWithTxtVidQueLesson.py
Library   TestCases/TrackWithVidDocQueLesson.py
Library   TestCases/TrackWithAllCardsOne.py
Library   TestCases/TrackWithAllCardsTwoTimes.py
Library   TestCases/TrackWithFourLessons.py
Library   TestCases/TrackWithFourLessonsDifferentCombiOfLessons.py
Library   TestCases/TrackWithFourLessonsDifferentCombiOfLessons2.py
Library   TestCases/TrackWithQuesLesssonAllCards1timeAllCards2TimeLessons.py


*** Test Cases ***
TC0 - User Login
    User Login

TC1 - BlankLessonFive
    Blank Lesson Five Main
    
TC2 - BlankLessonFiveTwo
    Blank Lesson Five Two Main
    
TC3 - BlankLessonOne
    Blank Lesson One Main
    
TC4 - BlankLessonTen
    Blank Lesson Ten Main
    
TC5 - BlankLessonTwo
    Blank Lesson Two Main  
    
TC6 - LessonExplainAConcept
    Lesson Explain A Concept Main
    
TC7 - TeachASkill
    Teach A Skill Main
    
    
    
TC8 - CreateCreator
    Create Creator User And Validation

TC9 - CreateLearner
    Create Learner User And Validation

TC10 - CreateLearnerAdministrator
    Create Learner Admin User And Validation
    
TC11 - CreateMasterAdmin
    Create Master Admin User And Validation
 
TC12 - UserAttributeListWithReq
    Create List Attribute With Required Field
    
TC13 - UserAttributeListWithoutReq
    Create List Attribute Without Required Field
           
TC14 - UserAttributeNumWithReq
    Create Number Attribute With Req
    
TC15 - UserAttributeNumWithoutReq
    Create Number Attribute Without Req
    
TC16 - UserAttributeTextWithReq
    Create Text Attribute With Req
    
TC17 - UserAttributeTextWithoutReq
    Create Text Attribute Without Req
    
TC18 - UserAttributeCheckboxWithReq
    Create Check Box Attribute With Req
    
TC19 - UserAttributeWithoutCheckbox
    Create Check Box Attribute Without Req
    
TC20 - UserAttributeDateWithReq
    Create Date Attribute With Req
    
TC21 - UserAttributeDateWithoutReq
    Create Date Attribute Without Req
    
TC22 - UserAttributeWithEmail
    Create Email Attribute With Req
    
TC23 - UserAttributeWithoutEmail
    Create Email Attribute Without Req

TC24 - LessonCreateImage
    Lesson With Image Upload Card
    
TC25 - LessonCreateVideo
    Lesson With Video Upload Card
    
TC26 - UserAttributeUserReferenceWithReq
    Create User Reference Attribute With Required Field
    
TC27 - UserAttributeUserReferenceWithoutReq
    Create User Reference Attribute Without Required Field
    
TC28 - TrackWithVidLessonDocLesssonQuesLesson
    Track With Two Lessons Vid Doc Ques
    
TC29 - TrackWithDocumentLesson
    Lesson With Document Card
    
TC30 - TrackWithImageLesson
    Lesson With Image Card
        
TC31 - TrackWithQuestionLesson
    TrackWithQuestionLesson.Lesson With Question Answer Card
    
TC32 - TrackWithTextLesson
    Track With Lesson Contains Text Card
    
TC33 - TrackWithTxtImgQueLesson
    Lesson With Text Image Question Card
    
TC34 - TrackWithVideoLesson
    Lesson With Video Card

TC35 - CreateTagDocLesson
    Creating Tag For Document Lesson
    
TC36 - CreateTagImageLesson
    Create Tag For Image Lesson
    
TC37 - CreateTagLessonCombinedLesson
    Create Tag For Combined Lesson
    
TC38 - CreateTagLessonExplainAconcept
    Create Tag For Lesson Explain A Concept

TC39 - CreateTagLessonIntroduceAtopic
    Create Tag For Lesson Introduce A Topic
    
TC40 - CreateTagLessonLimitedmultiplecardlesson_1
    Create Tag For Lesson Limited Multiple Card Lesson One
    
    
TC41 - CreateTagLessonLimitedmultiplecardlesson_2
    Create Tag For Lesson Limited Multiple Lesson Two
    
TC42 - CreateTagLessonLimitedmultiplecardlesson_3
    Create Tag For Lesson Limited Multiple Card Lesson Three
    
TC43 - CreateTagLessonMultiplecardlesson
    Create Tag For Lesson Multiple Card Lesson
    
TC44 - CreateTagLessonPowerpoint
    Create Tag For Lesson Power Point
    
TC45 - CreateTagLessonScorm
    Create Tag For Lesson Scorm
    
TC46 - CreateTagLessonTeachAskill   
    Create Tag For Lesson Teach A Skill
    
TC47 - CreateTagLessonTextLesson
    Create Tag For Lesson Textlesson
    
TC48 - CreateTagQuesLesson 
    Create Tag For Question Lesson
    
TC49 - CreateTagTrackLessonDocument   
    Create Tag For Track Lesson Document
    
TC50 - CreateTagTrackLessonFiveVideoDocumentQuestion  
    Create Tag For Track Lesson Five Video Document Question
    
TC51 - CreateTagTrackLessonImage  
    Create Tag For Track Lesson Image
    
    
TC52 - CreateTagTrackLessonOneTextImageVideoDocumentQuestion  
    Create Tag For Track Lesson One Text Image Video Document Question
    
    
TC53 - CreateTagTrackLessonQuestion
    Create Tag For Track Lesson Question
    
TC54 - CreateTagTrackLessonTenTextVideoQuestion
    Create Tag For Track Lesson Ten Text Video Question
    
TC55 - CreateTagTrackLessonTwoTextImageVideoDocumentQuestion
    Create Tag For Track Lesson Two Text Image Video Document Question
    
TC56 - CreateTagTrackLessonVideo
    Create Tag For Track Lesson Video
    
    
TC57 - CreateTagTrackWithfourlessons10_12_3
    Create Tag For Track With Four Lessons Ten Twelve Three
    
TC58 - CreateTagTrackWithfourlessons4_5_6_7
    Create Tag For Track With Four Lessons Four Five Six Seven

      
TC59 - CreateTagTrackWithfourlessons78910
    Create Tag For Track With Four Lesson Seven Eight Nine Ten
    
TC60 - CreateTagTrackWithonelesson_9
    Create Tag For Track With One Lesson Nine
    
TC61 - CreateTagTrackWiththreelessons_3_4_5
    Create Tag For Track With Three Lessons Three Four Five
    
TC62 - CreateTagTrackWiththreelessons_5_6_7
    Create Tag For Track With Three Lessons Five Six Seven
    
TC63 - CreateTagTracklessonFiveTextImageQuestion
    Create Tag For Track Lesson Five Text Image Question
    
TC64 - CreateTagTrackWithTwolessons_1_2
    Create Tag For Track With Two Lessons One Two
    
TC65 - CreateTagTrackWithTwolessons_2_3
    Create Tag For Track With Two Lessons Two Three

TC66 - CreateTagVideoLesson
    Create Tag For Video Lesson
   
    
TC67 - LessonCreateDocument 
    Lesson With Document Upload Card
       
TC68 - LessonCreateQuestion
    LessonCreateQuestion.Lesson With Question Answer Card
    
TC69 - LessonCreateText
    LessonCreateText.Lesson With Text Card
    
TC70 - TrackWithImgLessonVidLesson
    Track With Two Lessons Imgand Vid
    
TC71 - TrackWithTxtLessonImgLesson
    Track With Txt Lesson Image Lesson
    
TC72 - TrackWithTxtVidQueLesson
    Lesson With Text Video Question Card
    
TC73 - TrackWithVidDocQueLesson 
    Lesson With Video Document Question Card
    
TC74 - TrackWithAllCardsOne
    Track With All Cards

TC75 - TrackWithAllCardsTwoTimes
    Track With All Card Two Time
    
TC76 - TrackWithFourLessons
    Track With Four Lesson
    
TC77 - TrackWithFourLessonsDifferentCombiOfLessons
    Track With Four Lessons Diff Combi 1
    
TC78 - TrackWithFourLessonsDifferentCombiOfLessons2
    Track With Four Lessons Different Combi 2
    
TC79 - TrackWithQuesLesssonAllCards1timeAllCards2TimeLessons
    Track With Ques All Card One And Two Time Lessons
    
    
    
    
    
    
    
    
    
    
    
    
