'''
Created on Mar 16, 2018

@author: Shavinlal E
'''
from os.path import os
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from BaseTestClass import BaseTestClass
from BaseTestClass import driver


# create a new Firefox session
class LessonDuplicate:
    
    
    def CreateLessonForDuplicating(self):   
        
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
        
    def lessonWithTextCardforduplicate(self):   
        
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
        
    def addQuestionCardforduplicate(self):
        
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
        
    def addImageCardforduplicate(self,time):
        
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
        

    def addVideoCardforduplicate(self,time):
        
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
     
        
    def addDocumentCardforduplicate(self,time):
        
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
        
    def publishLessonduplicate(self): 
        
        wait=WebDriverWait(driver, 80)
        wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button").click()
        
        print "Clicking on READY TO PUBLISH button"
        #wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]").click()
        
        print "Clicking on PUBLISH button"
        """print "Validating the success message after publish"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[2]/div/div/span[2]"))) 
        
        actual_success_message= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[2]/div/div/span[2]").text
        
        expected_success_message= "You have successfully published \"" + lesson_title + "\""; 
        
        if(expected_success_message==actual_success_message):
            print "The success message is displaying as"+ " "+expected_success_message
        else:
            print "The success message is not displaying as expected"
            """
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[1]/a").click()
        print "Clicking on EXIT button"
             
        print "Verifying lesson displayed in Grid"
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td[2]/a[.='"+lesson_title+"'])[1]")))

        if driver.find_element_by_xpath("(//tbody/tr/td[2]/a[.='"+lesson_title+"'])[1]").is_displayed():
            print "Lesson is displayed in Grid ::"+lesson_title
        else:
            print "Lesson not displaying in grid"
            raise Exception
        
        # Going to click on duplicate link for the published lesson
        driver.find_element_by_xpath("//table/tbody/tr/td[2]/a[.='"+lesson_title+"']/../../td[4]/button[1]").click()
        print "Clicking on Duplicate link for published lesson"+" "+ lesson_title
        
        # Going to verify the content in the Duplicate lesson pop up
        
        print "Going to verify the content in the Duplicate lesson pop up"
        
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('MultiCardLesson')
        cell9= first_sheet.cell(61,0)
        
        
        wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[2]/div/div/div[1]/h3")))
        expectedPopUpHeader = cell9.value 
        actualPopUpHeader = driver.find_element_by_xpath("html/body/div[2]/div/div/div[1]/h3").text
        
        
        cell10= first_sheet.cell(61,1)
        expectedPopUpBody1= cell10.value+'"'+lesson_title+'"'
        actualPopUpBody1 = driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/h3").text
        
        
        cell11= first_sheet.cell(61,2)
        expectedFieldName = cell11.value
        actualFieldName = driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[1]/div/label").text
        
        cell12 = first_sheet.cell(61,3)
        expectedNameOfCopy = cell12.value + " "+lesson_title
        actualNameOfCopy = driver.find_element_by_xpath(".//*[@id='lesson-title-duplicate']").get_attribute('value')
        
        
        cell13 = first_sheet.cell(61,4)
        expectedButtonName1 = cell13.value
        actualButtonName1 = driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[2]/button[2]").text
        
        cell14 = first_sheet.cell(61,5)
        expectedButtonName2 = cell14.value
        actualButtonName2 = driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[2]/button[1]").text
        
        closeIcon= driver.find_element_by_xpath("html/body/div[2]/div/div/div[1]/button")
        

        if(expectedPopUpHeader == actualPopUpHeader):
            if(expectedPopUpBody1 == actualPopUpBody1):
                if (expectedFieldName == actualFieldName):
                    if (expectedNameOfCopy == actualNameOfCopy):
                        if (expectedButtonName1 == actualButtonName1):
                            if (expectedButtonName2 == actualButtonName2):
                                if (closeIcon.is_displayed()):
                    
                                    print "Successfully verified the contents in Duplicate lesson pop up"
        else:
            
            print "Failed to verify the contents in Duplicate lesson pop up"    
            raise Exception
        
        
        # Going to edit the autopopulated name of lesson copy
        
        print "Going to clear the autopopulated name and enter new name for the duplicate lesson"
        
        driver.find_element_by_xpath(".//*[@id='lesson-title-duplicate']").click()
        driver.find_element_by_xpath(".//*[@id='lesson-title-duplicate']").clear()
        
        driver.find_element_by_xpath(".//*[@id='lesson-title-duplicate']").send_keys("Copy of"+" "+lesson_title)
        print "Cleard the autopopulated name and Entered new name for duplicate lesson"
        
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[2]/button[1]").click()
        print "Clicking on save button"
        
        duplicate_lesson_title = "Copy of"+" "+lesson_title
        
        print "Check if the created duplicate lesson is displayed in Grid with status as Draft"
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td[2]/a[.='"+lesson_title+"'])[1]")))

        if driver.find_element_by_xpath("//table/tbody/tr/td[.='Draft']/../td[2]/a[.='"+duplicate_lesson_title+"']").is_displayed():
            print "Duplicate Lesson with status as Draft is displaying in Grid ::"+duplicate_lesson_title
        else:
            print "Duplicate Lesson is not displaying in grid"
            raise Exception

        
        
        

    def duplicateLessonMain(self): 
        
        try: 
            obj1 = LessonDuplicate()
            obj1.CreateLessonForDuplicating()
            obj1.lessonWithTextCardforduplicate()
            obj1.addQuestionCardforduplicate()
            obj1.addImageCardforduplicate(600)
            obj1.addVideoCardforduplicate(600)
            obj1.addDocumentCardforduplicate(600)
            obj1.publishLessonduplicate()
            
            
            print "TEST CASE EXECUTED SUCCESSFULLY COMPLETED"
        except Exception as e:
            traceback.print_exc()
            print (e)
            raise Exception
            
        finally:
            print "clicking on Home"
            book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
            first_sheet = book.sheet_by_name('Login_Credentials')
            print("Fetching the Attribute Name from Excel Sheet\n")
            # read a cell
            cell = first_sheet.cell(1,1)
            HomeURL = cell.value
            print HomeURL
            driver.get(HomeURL)
            print "Home Page Loaded"
     
       
if __name__ == '__main__':
    
    obj11= LessonDuplicate()
    obj12= BaseTestClass()
    obj12.UserLogin()
    obj11.duplicateLessonMain()
  
    print "Test executed successfully"
             
        
        
        
        