'''
Created on Feb 22, 2018

@author: Shavinlal E
'''
from os.path import os
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait, expected_conditions as EC
import xlrd
from selenium.webdriver.support.ui import WebDriverWait
from BaseTestClass import driver


# create a new Firefox session
class BlankLessonFiveTwo:
        
    def lessonWithTitletCard(self,lesson_title):   
        
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/lessons']")))

        print "Clicking on Lessons button from side menu"
        driver.find_element_by_xpath("//a[@href='/create/lessons']").click()
    
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div/button")))  
        print "Clicking on Create Lesson button from lessons page"
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/header/div/button").click()
       
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[2]/div/div")))  
        print "Clicking on BlankLesson + icon from Create a new lesson pop up"
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[2]/div/div").click()
       
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[1]/span")))  
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").send_keys(lesson_title)
        print "Entering the lesson title in title card as"+" "+lesson_title
          
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']"))) 
        
        
    def lessonWithTextCard(self,TextContent):   
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div").click()
        print "Clicking on Add card + icon"  
         
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div").click()
        print "Clicking on Text card"    
     
         
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']"))) 
        element = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div")
        webdriver.ActionChains(driver).move_to_element(element).click().send_keys(TextContent).perform()
        print "Entering the text as"+ " "+TextContent 
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']"))) 
      
        
    def addQuestionCard(self,questionCard,ans1,ans2):
        
        wait=WebDriverWait(driver, 60)
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div"))) 
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div").click()
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
        
    def addImageCard(self,Imagefilepath1,linkname,Imagefilepath2,time):
        
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
        
        print "Going to upload the image file"
        
        driver.find_element_by_css_selector('input[type="file"]').send_keys(Imagefilepath1)
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/img")))
        
        imageContainerlocator_after1upload= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/img")
        
        if(imageContainerlocator_after1upload.is_displayed()):
            
            print 'Successfully uploaded the image1 file'
            
        else:
            print "Failed to upload the image1 file"
            raise Exception 
        
        
        '''print "Going to delete the image1"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[2]/button").click()
        
        browseforyourlink=  driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div[1]/h4/div[1]/span[2]")
        
        if(browseforyourlink.is_displayed() and browseforyourlink.text==linkname):
            
            print 'Successfully deleted the image1 file'
            
        else:
            print "Failed to delete the image file"
            raise Exception 
        
        
        print "Going to upload second image file"
        
        driver.find_element_by_css_selector('input[type="file"]').send_keys(Imagefilepath2)
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/img")))
        imageContainerlocator_after2upload= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/img")
        
        if(imageContainerlocator_after2upload.is_displayed()):
            
            print 'Successfully uploaded the image2 file'
            
        else:
            print "Failed to upload the image2 file"
            raise Exception 
        
        print "Going to delete the uploaded image2 and inserting an animated GIF"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[2]/button").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div[1]/h4/div[2]/span[2]")))
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div[1]/h4/div[2]/span[2]").click()
        print "Clicking on insert animated GIF link"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[2]/div/ul/li[1]/div")))
        
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[2]/div/ul/li[1]/div").click()
        print "Selecting the first GIF from"+" "+"Search all the GIFs pop up"
        
        wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[2]/div/div/div[2]/div[3]/button[1]")))
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[3]/button[1]").click()
        print "Clicking on SAVE button"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]")))
        
        GifLocator= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]")
        
        if(GifLocator.is_displayed()):
            
            print "The GIF added successfully" 
           
        else:
            
            print "Failed to add GIF"
            raise Exception 
        '''
        '''
        print "Going to delete the added GIF"
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[2]/button[2]").click()
       
        insertAnimatedGIFlinklocator= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div[1]/h4/div[2]/span[2]")
        
        
        if(insertAnimatedGIFlinklocator.is_displayed()):
            
            print "The GIF deleted successfully" 
           
        else:
            
            print "Failed to delete added GIF"
            raise Exception 
        '''
        
    def addVideoCard(self,videoName,time):
        
        wait=WebDriverWait(driver, time)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div")))
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div").click()
        print "Clicking on Add card + icon"
        
        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]").click()
        
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
     
        
    def addDocumentCard(self,document1Path,time):
        
        wait=WebDriverWait(driver, time)
         
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div").click()
        print "Clicking on Add card + icon"   
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[4]/div[1]/div").click()
        print "Selecting the Document card"
        
        
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
        
        
        # Going to delete the uploaded file
        
        ''' driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[2]/button").click()
        print "Clicking on Delete button displayed for uploaded file"
        
        browseForYourFileLink= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div[1]/h4/div")
        
        if (browseForYourFileLink.is_displayed()):
            
            print "Successfully deleted the file"
           
        
        else:
            
            print "Failed to delete the file"
            raise Exception
        '''
        
        
       
        
        # Going to upload another file
        
        #driver.find_element_by_css_selector('input[type="file"]').send_keys(document2Path)
        #print "Uploading second document file"
        
        #wait till the red color border is displaying
        
        #wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div[3]")))
        
        #redColorBoreder =  driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div[3]")
     
     
        #if (redColorBoreder.is_displayed()):
            
           # print "The document in path"+ " "+document2Path+" "+"is failing to upload"
        
       # else:
            
         #   print "Document format validation fails"
         #   raise Exception
        
        #print "Going to click on Change Image button"
        
        #driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div").click()
        
        #print "Clicking on Change Image button"
        #driver.find_element_by_css_selector('input[type="file"]').send_keys(Imagefilepath3)
        
        
        
        
        
    def publishLesson(self,lesson_title): 
        
        wait=WebDriverWait(driver, 60)
        #wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        #wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']"))) 
      
        wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button").click()
        print "Clicking on READY TO PUBLISH button"
         
        
        #wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]").click()
        print "Clicking on PUBLISH button"
        
        #print "Validating the success message after publish"
        #wait=WebDriverWait(driver, 60) 
        #wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[2]/div/div/span[2]"))) 
        #actual_success_message= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[2]/div/div/span[2]").text
        #expected_success_message= "You have successfully published \"" + lesson_title + "\""; 
        
        #if(expected_success_message==actual_success_message):
            
           # print "The success message is displaying as"+ " "+expected_success_message
            
        #else:
            
            #print "The success message is not displaying as expected"
            
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[1]/a").click()
        print "Clicking on EXIT button"
        
        
             
        print "Verifying lesson displayed in Grid"
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td[2]/a[.='"+lesson_title+"'])[1]")))

        if driver.find_element_by_xpath("(//tbody/tr/td[2]/a[.='"+lesson_title+"'])[1]").is_displayed():
            
            print "Lesson is displayed in Grid ::"+lesson_title
            
        else:
            print "Lesson not displaying in grid"
        
        
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[4]").click()
        
    def blankLessonFiveTwoMain(self): 
        
        try :
        
            book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
            first_sheet = book.sheet_by_name('MultiCardLesson')
            
            cell1 = first_sheet.cell(9,0)
            blankLessonFiveTwoname = cell1.value
            
            cell2 = first_sheet.cell(2,2)
            blankLessonFiveTwoQuestion = cell2.value
            
            cell3 = first_sheet.cell(1,3)
            blankLessonFiveTwoQuestionOption1 = cell3.value
            
            cell4 = first_sheet.cell(1,4)
            blankLessonFiveTwoQuestionOption2 = cell4.value
           
            cell5 = first_sheet.cell(1,8)
            blankLessonFiveTwoVideoCard = cell5.value
        
    
            cell6 = first_sheet.cell(1,9)
            blankLessonFiveTwoDocumentCard = cell6.value 
               
            
            obj1 = BlankLessonFiveTwo()
            obj1.lessonWithTitletCard(blankLessonFiveTwoname)
            obj1.addQuestionCard(blankLessonFiveTwoQuestion,blankLessonFiveTwoQuestionOption1,blankLessonFiveTwoQuestionOption2)
            obj1.addQuestionCard(blankLessonFiveTwoQuestion,blankLessonFiveTwoQuestionOption1,blankLessonFiveTwoQuestionOption2)
            obj1.addQuestionCard(blankLessonFiveTwoQuestion,blankLessonFiveTwoQuestionOption1,blankLessonFiveTwoQuestionOption2)
            obj1.addQuestionCard(blankLessonFiveTwoQuestion,blankLessonFiveTwoQuestionOption1,blankLessonFiveTwoQuestionOption2)
            obj1.addQuestionCard(blankLessonFiveTwoQuestion,blankLessonFiveTwoQuestionOption1,blankLessonFiveTwoQuestionOption2)
            obj1.addVideoCard(blankLessonFiveTwoVideoCard,600)
            obj1.addVideoCard(blankLessonFiveTwoVideoCard,600)
            obj1.addVideoCard(blankLessonFiveTwoVideoCard,600)
            obj1.addVideoCard(blankLessonFiveTwoVideoCard,600)
            obj1.addVideoCard(blankLessonFiveTwoVideoCard,600)
            obj1.addDocumentCard(blankLessonFiveTwoDocumentCard,600)
            obj1.addDocumentCard(blankLessonFiveTwoDocumentCard,600)
            obj1.addDocumentCard(blankLessonFiveTwoDocumentCard,600)
            obj1.addDocumentCard(blankLessonFiveTwoDocumentCard,600)
            obj1.addDocumentCard(blankLessonFiveTwoDocumentCard,600)
            obj1.publishLesson(blankLessonFiveTwoname)
            print "Test executed successfully"
        
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
            wait=WebDriverWait(driver, 80)
            wait.until(EC.visibility_of_element_located((By.ID,"global-header-search")))
            print "Home Page Loaded"
        
