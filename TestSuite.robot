*** Settings ***
Library   BaseTestClass.py

Library   BlankLessonFive.py
Library   BlankLessonFiveTwo.py
Library   BlankLessonOne.py
Library   BlankLessonTen.py
Library   BlankLessonTwo.py
Library   LessonExplainAConcept.py
Library   TeachASkill.py


Library   CreateCreator.py
Library   CreateLearner.py
Library   CreateLearnerAdministrator.py
Library   CreateMasterAdmin.py
Library   CreateTagDocLesson.py
Library   CreateTagImageLesson.py
Library   CreateTagLessonCombinedLesson.py
Library   CreateTagLessonExplainAconcept.py
Library   CreateTagLessonIntroduceAtopic.py
Library   CreateTagLessonLimitedmultiplecardlesson_1.py
Library   CreateTagLessonLimitedmultiplecardlesson_2.py
Library   CreateTagLessonLimitedmultiplecardlesson_3.py
Library   CreateTagLessonMultiplecardlesson.py
Library   CreateTagLessonPowerpoint.py
Library   CreateTagLessonScorm.py
Library   CreateTagLessonTeachAskill.py
Library   CreateTagLessonTextLesson.py
Library   CreateTagQuesLesson.py
Library   CreateTagTrackLessonDocument.py
Library   CreateTagTrackLessonFiveVideoDocumentQuestion.py
Library   CreateTagTrackLessonImage.py
Library   CreateTagTrackLessonOneTextImageVideoDocumentQuestion.py
Library   CreateTagTrackLessonQuestion.py
Library   CreateTagTrackLessonTenTextVideoQuestion.py
Library   CreateTagTrackLessonTwoTextImageVideoDocumentQuestion.py
Library   CreateTagTrackLessonVideo.py
Library   CreateTagTrackWithTwolessons_1_2.py
Library   CreateTagTrackWithTwolessons_2_3.py
Library   CreateTagTrackWithfourlessons10_12_3.py
Library   CreateTagTrackWithfourlessons4_5_6_7.py
Library   CreateTagTrackWithfourlessons78910.py
Library   CreateTagTrackWithonelesson_9.py
Library   CreateTagTrackWiththreelessons_3_4_5.py
Library   CreateTagTrackWiththreelessons_5_6_7.py
Library   CreateTagTracklessonFiveTextImageQuestion.py
Library   CreateTagVideoLesson.py
Library   UserAttributeCheckboxWithReq.py
Library   UserAttributeWithoutCheckbox.py
Library   UserAttributeDateWithReq.py
Library   UserAttributeDateWithoutReq.py
Library   UserAttributeListWithReq.py
Library   UserAttributeListWithoutReq.py
Library   UserAttributeNumWithReq.py
Library   UserAttributeNumWithoutReq.py
Library   UserAttributeTextWithReq.py
Library   UserAttributeTextWithoutReq.py
Library   UserAttributeUserReferenceWithReq.py
Library   UserAttributeUserReferenceWithoutReq.py
Library   UserAttributeWithEmail.py
Library   UserAttributeWithoutEmail.py



Library   LessonCreateImage.py
Library   LessonCreateVideo.py
Library   TrackWithDocumentLesson.py
Library   TrackWithImageLesson.py
Library   TrackWithQuestionLesson.py
Library   TrackWithTextLesson.py
Library   TrackWithTxtImgQueLesson.py
Library   TrackWithVideoLesson.py
Library   TrackWithVidLessonDocLesssonQuesLesson.py
Library   LessonCreateDocument.py
Library   LessonCreateQuestion.py
Library   LessonCreateText.py
Library   TrackWithImgLessonVidLesson.py
Library   TrackWithTxtLessonImgLesson.py
Library   TrackWithTxtVidQueLesson.py
Library   TrackWithVidDocQueLesson.py
Library   TrackWithAllCardsOne.py
Library   TrackWithAllCardsTwoTimes.py
Library   TrackWithFourLessons.py
Library   TrackWithFourLessonsDifferentCombiOfLessons.py
Library   TrackWithFourLessonsDifferentCombiOfLessons2.py
Library   TrackWithQuesLesssonAllCards1timeAllCards2TimeLessons.py


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
    
    
    
    
    
    
    
    
    
    
    
    