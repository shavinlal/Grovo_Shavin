'''
Created on Mar 15, 2018

@author: Shavinlal E
'''
from os.path import os
import time
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from BaseTestClass import BaseTestClass
from BaseTestClass import driver


# create a new Firefox session
class LessonEdit:
    
    
    def editCreatedLesson(self):   
        
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/lessons']")))

        print "Clicking on Lessons button from side menu"
        driver.find_element_by_xpath("//a[@href='/create/lessons']").click()
    
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div/button")))  
        print "Clicking on Create Lesson button from lessons page"
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/header/div/button").click()
       
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[2]/div/div")))  
        
        print "Clicking on BlankLesson + icon from Create a new lesson pop up"
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[2]/div/div").click()
       
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('MultiCardLesson')
          
        cell1= first_sheet.cell(59,0)
        global lesson_title
        lesson_title = cell1.value   

        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[1]/span")))  
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").send_keys(lesson_title)
        print "Entering the lesson title in title card as"+" "+lesson_title
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']"))) 
        
    def lessonWithTextCardforedit(self):   
        
        wait=WebDriverWait(driver, 60)
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div").click()
        
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('MultiCardLesson')
        cell2= first_sheet.cell(59,1)
        TextContent = cell2.value 
        
        print "Clicking on Add card + icon"  
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div").click()
        
        print "Clicking on Text card"    
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']"))) 
        
        element = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div")
        webdriver.ActionChains(driver).move_to_element(element).click().send_keys(TextContent).perform()
        
        print "Entering the text as"+ " "+TextContent 
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']"))) 
        
    def addQuestionCardforedit(self):
        
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div"))) 
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div").click()
        
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('MultiCardLesson')
        
        cell3= first_sheet.cell(59,2)
        questionCard = cell3.value 
        
        cell4= first_sheet.cell(1,3)
        ans1 = cell4.value 
        
        cell5= first_sheet.cell(1,4)
        ans2 = cell5.value 

        
        print "Clicking on Add card + icon"  
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[5]/div[1]/div").click()
        
        print "Question card selected"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='question-answer-input-0']")))
        
        print "Entering question"
        ele=driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/p/textarea")
        ele.send_keys(questionCard)
        
        print "Entering first answer"
        driver.find_element_by_xpath(".//*[@id='question-answer-input-0']").send_keys(ans1)
        
        print "Entering Second answer"
        driver.find_element_by_xpath(".//*[@id='question-answer-input-1']").send_keys(ans2)
          
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']"))) 
        
    def addImageCardforedit(self,time):
        
        wait=WebDriverWait(driver, time)
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div").click()
        
        print "Clicking on Add card + icon"
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div").click()
        
        print "Image card selected"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div[1]/h4/div[1]/span[2]/div")))
        #driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div[1]/h4/div[1]/span[2]/div").click()
        #print "Clicking on browse for your file link"
     
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']"))) 
        
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('MultiCardLesson')
        cell6= first_sheet.cell(1,5)
        Imagefilepath1 = cell6.value 
        
        
        
        print "Going to upload the image file"
        driver.find_element_by_css_selector('input[type="file"]').send_keys(Imagefilepath1)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/img")))
        
        imageContainerlocator_after1upload= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/img")
        
        if(imageContainerlocator_after1upload.is_displayed()):
            print 'Successfully uploaded the image1 file'
        else:
            print "Failed to upload the image1 file"
            raise Exception 
        

    def addVideoCardforedit(self,time):
        
        wait=WebDriverWait(driver, time)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div").click()
        
        print "Clicking on Add card + icon"
        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]").click()
        
                
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('MultiCardLesson')
        cell7= first_sheet.cell(1,8)
        videoName = cell7.value 
        
        
        
        #Uploading Video
        print "Uploading Video"
        driver.find_element_by_css_selector('input[type="file"]').send_keys(videoName)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/button")))
        
        videoContainerlocator_afterupload= driver.find_element_by_xpath("html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/button")
        
        if(videoContainerlocator_afterupload.is_displayed()):
            print 'Successfully uploaded the Video file'
        else:
            print "Failed to upload the Video file"
            raise Exception
        
        driver.find_element_by_xpath("html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/button").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div")))
     
        
    def addDocumentCardforedit(self,time):
        
        wait=WebDriverWait(driver, time)
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div").click()
        
        print "Clicking on Add card + icon"   
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[4]/div[1]/div").click()
        
        print "Selecting the Document card"
        
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('MultiCardLesson')
        cell8= first_sheet.cell(1,9)
        document1Path = cell8.value 
        
        driver.find_element_by_css_selector('input[type="file"]').send_keys(document1Path)
        print "Uploading document file"
        
        #wait till minimize button is displayed
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/div[1]/button[1]")))
        
        downloadButtonLocator= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[2]/div/div/div[1]/div/a")
        
        if (downloadButtonLocator.is_displayed()):
            
            print "The file has been uploaded successfully"
        else:
            print "Failed to upload the file"
            raise Exception
        
    def publishLessonedit(self):
        
        wait=WebDriverWait(driver, 60)
        wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button").click()
    
        
        print "Clicking on READY TO PUBLISH button"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]").click()
        
        print "Clicking on PUBLISH button"
        """   
        print "Validating the success message after publish"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[2]/div/div/span[2]"))) 
        
        actual_success_message= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[2]/div/div/span[2]").text
        
        expected_success_message= "You have successfully published \"" + lesson_title + "\""; 
        
        if(expected_success_message==actual_success_message):
            print "The success message is displaying as"+ " "+expected_success_message
        else:
            print "The success message is not displaying as expected"
         """
            
        # wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[2]/div/div/span[2]"))) 
        time.sleep(6)
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[1]/a").click()
        print "Clicking on EXIT button"
             
        print "Verifying lesson displayed in Grid"
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td[2]/a[.='"+lesson_title+"'])[1]")))

        if driver.find_element_by_xpath("(//tbody/tr/td[2]/a[.='"+lesson_title+"'])[1]").is_displayed():
            print "Lesson is displayed in Grid ::"+lesson_title
        else:
            print "Lesson not displaying in grid"
            raise Exception
        
    def clickEdit(self):  
              
        wait=WebDriverWait(driver, 80)
        # Going to click on edit for the created lesson 
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"//table/tbody/tr/td[.='Published']/../td[2]/a[.='"+lesson_title+"']")))
        driver.find_element_by_xpath("//table/tbody/tr/td[.='Published']/../td[2]/a[.='"+lesson_title+"']/../../td[4]/a[.='Edit']").click()
        print "Clicking on edit link for the created lesson"+ " "+lesson_title
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[1]/a")))
        
        # Going to verify the lesson title
       
        actuale_lesson_title = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").text

        if (actuale_lesson_title == lesson_title):
        
            print "The edit page is displaying for the published lesson"

        else:
            
            print "Failed to open the edit page for published lesson"
            raise Exception
        
        # Going to clear the lesson title
        
        print "Going to edit the lesson title"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").clear()
        print "Cleared the lesson title"
        
        new_lesson_title = "Edited_title"+" "+lesson_title
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").send_keys(new_lesson_title)
        print "Re-entered the lesson title"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']"))) 
        
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div/div/div[2]/div/div[1]").click()
        print "Selecting the Text card" 
        
        #Going to clear the content
        print "Going to clear the content in text card"
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div").clear()
        
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('MultiCardLesson')
        cell9= first_sheet.cell(59,3)
        editedText = cell9.value 
        
        textElement = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div")
        webdriver.ActionChains(driver).move_to_element(textElement).click().send_keys(editedText).perform()
        
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']"))) 
        
  
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div/div/div[3]/div/div[1]").click()
        print "Selecting the Question Card" 
        
        cell10= first_sheet.cell(59,4)
        questionAfterEdit = cell10.value 
         
        print "Entering question"
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/p/textarea").send_keys(questionAfterEdit)

        cell11= first_sheet.cell(59,5)
        firstAnswerAfterEdit = cell11.value 
        
        print "Entering first answer"
        driver.find_element_by_xpath(".//*[@id='question-answer-input-0']").send_keys(firstAnswerAfterEdit)
        
        cell12= first_sheet.cell(59,6)
        secondAnswerAfterEdit = cell12.value 
        
        print "Entering Second answer"
        driver.find_element_by_xpath(".//*[@id='question-answer-input-1']").send_keys(secondAnswerAfterEdit)
          
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']"))) 
        
        
        # Clicking on Image card 
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div/div/div[4]/div/div[1]").click()
        print "Selecting the Image card"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[2]/button").click()
        print "Clicking on Delete button"
        
        print "Going to upload the image file"
        
        cell13= first_sheet.cell(1,5)
        Imagefilepath2 = cell13.value 
        
        wait=WebDriverWait(driver,600)
        driver.find_element_by_css_selector('input[type="file"]').send_keys(Imagefilepath2)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/img")))
        
        imageContainerlocator_after1upload= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/img")
        
        if(imageContainerlocator_after1upload.is_displayed()):
            print 'Successfully uploaded the image2 file'
        else:
            print "Failed to upload the image2 file"
            raise Exception 
        
        # Clicking on Video card 
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div/div/div[5]/div/div[1]").click()
        print "Selecting the Video card"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[2]/button").click()
        print "Clicking on Delete button"
        
        cell14= first_sheet.cell(1,8)
        videoName1 = cell14.value 
        
    
        #Uploading Video
        print "Uploading new Video"
        driver.find_element_by_css_selector('input[type="file"]').send_keys(videoName1)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/button")))
        
        videoContainerlocator_afterupload= driver.find_element_by_xpath("html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/button")
        
        if(videoContainerlocator_afterupload.is_displayed()):
            print 'Successfully uploaded the Video file'
        else:
            print "Failed to upload the Video file"
            raise Exception
        
        driver.find_element_by_xpath("html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/button").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div")))
     
        
        # Clicking on Document card 
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div/div/div[6]/div/div[1]").click()
        print "Selecting the Document card"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[2]/button").click()
        print "Clicking on Delete button"
        
        cell15= first_sheet.cell(1,9)
        document2Path = cell15.value 
        
        driver.find_element_by_css_selector('input[type="file"]').send_keys(document2Path)
        print "Uploading new document file"
        
        #wait till minimize button is displayed
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/div[1]/button[1]")))
        
        downloadButtonLocator= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[2]/div/div/div[1]/div/a")
        
        if (downloadButtonLocator.is_displayed()):
            
            print "The new file has been uploaded successfully"
        else:
            print "Failed to upload the file"
            raise Exception
        
        
        
        wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button").click()
    
        
        print "Clicking on READY TO PUBLISH button"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]").click()
        
        print "Clicking on PUBLISH button"
        """   
        print "Validating the success message after publish"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[2]/div/div/span[2]"))) 
        
        actual_success_message= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[2]/div/div/span[2]").text
        
        expected_success_message= "You have successfully published \"" + lesson_title + "\""; 
        
        if(expected_success_message==actual_success_message):
            print "The success message is displaying as"+ " "+expected_success_message
        else:
            print "The success message is not displaying as expected"
         """
            
        # wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[2]/div/div/span[2]"))) 
        time.sleep(6)
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[1]/a").click()
        print "Clicking on EXIT button"
             
        print "Verifying lesson displayed in Grid"
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td[2]/a[.='"+new_lesson_title+"'])[1]")))

        if driver.find_element_by_xpath("(//tbody/tr/td[2]/a[.='"+new_lesson_title+"'])[1]").is_displayed():
            print "Lesson is displayed in Grid ::"+new_lesson_title
        else:
            print "Lesson not displaying in grid"
            raise Exception

        

    def lessonEditMain(self):    
        
        try:
            obj1 = LessonEdit()
            obj1.editCreatedLesson()
            obj1.lessonWithTextCardforedit()
            obj1.addQuestionCardforedit()
            obj1.addImageCardforedit(600)
            obj1.addVideoCardforedit(600)
            obj1.addDocumentCardforedit(600)
            obj1.publishLessonedit()
            obj1.clickEdit()
            print "TEST CASE EXECUTION SUCCESSFULLY COMPLETED"
        except Exception as e:
            traceback.print_exc()
            print (e)
            raise Exception
            
        finally:
            #print "clicking on Home"
            book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
            first_sheet = book.sheet_by_name('Login_Credentials')
            #print("Fetching the Attribute Name from Excel Sheet\n")
            # read a cell
            cell = first_sheet.cell(1,1)
            HomeURL = cell.value
            #print HomeURL
            driver.get(HomeURL)
            #print "Home Page Loaded"
        
     
           
if __name__ == '__main__':
    
    obj11= LessonEdit()
    obj12= BaseTestClass()
    obj12.UserLogin()
    obj11.lessonEditMain()
  
    print "Test executed successfully"
