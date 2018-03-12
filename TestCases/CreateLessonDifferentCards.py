'''
Created on 07-Mar-2018

@author: dattatraya
'''


from BaseTestClass import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CreateLessonDifferentCards:
    
    def textCard(self,textCard):
        print "Text card"
        print "Click on (+) icon"
            
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div/span").click()
    
        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]").click()
            
        textCardelement=driver.find_element_by_xpath("//div[@class='text']/div/div[1]/div")
            
        #Entering Text in Text card 
            
        webdriver.ActionChains(driver).move_to_element(textCardelement).click().send_keys(textCard).perform()
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']")))
            
        #Verifying entered text is displaying text card
        print "Verifying entered text is displaying text card"
            
        textAfterEntering=driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/span/span").text
            
        if textAfterEntering==textCard:
            print "Verified Text '"+textCard+"' is displayed in Text Card"
        else:
            print "Text not displayed in Text card"
            raise Exception
        
    def imageCard(self,Imagefilepath1):
        print "\nUploading Image"
        wait=WebDriverWait(driver, 60)
        print "Click on (+) icon"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div/span").click()
        
        #Clicking on Image card
        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[1]").click()
        
        #Uploading image
        driver.find_element_by_css_selector('input[type="file"]').send_keys(Imagefilepath1)
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/img")))
        
        imageContainerlocator_after1upload= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/img")
        
        if(imageContainerlocator_after1upload.is_displayed()):
            
            print 'Successfully uploaded the image1 file'
            
        else:
            print "Failed to upload the image1 file"
            raise Exception
        
    def videoCard(self,videoPath,timeToUploadVideo):
        print "Click on (+) icon"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div/span").click()
        
        #Clicking on Video card
        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]").click()
        
        #Uploading Video
        print "Uploading Video"
        driver.find_element_by_css_selector('input[type="file"]').send_keys(videoPath)
        
        WebDriverWait(driver, timeToUploadVideo).until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/button")))
        
        videoContainerlocator_afterupload= driver.find_element_by_xpath("html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/button")
        
        if(videoContainerlocator_afterupload.is_displayed()):
            
            print "Successfully uploaded the Video file"
            
        else:
            print "Failed to upload the Video file"
            raise Exception
        
        
    
    
    def docCard(self,documentPath,timetoUploadDoc):
        print "Document"
        print "Click on (+) icon"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div/span").click()
        
        #Clicking on Document card
        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[4]/div[1]/div").click()
        
        
        
        #Uploading Document
        print "Uploading Document"
        driver.find_element_by_css_selector('input[type="file"]').send_keys(documentPath)
        
        WebDriverWait(driver, timetoUploadDoc).until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/label")))
        
        documentContainerlocator_afterupload= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/label")
        
        if(documentContainerlocator_afterupload.is_displayed()):
            
            print "Successfully uploaded the Video file"
            
        else:
            print "Failed to upload the Document file"
            raise Exception
        
        
    def quesCard(self,questionCard,ans1,ans2):
        print "\nInserting Question card"
        wait=WebDriverWait(driver, 60)

        print "Click on (+) icon"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div/span").click()
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[5]/div[1]/div").click()
        
        print "Question card selected"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='question-answer-input-0']")))
        print "Entering question"
        questionArea=driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/p/textarea")
        questionArea.send_keys(questionCard)
        print "Question entered ::"
        
        print "Entering first answer"
        driver.find_element_by_xpath(".//*[@id='question-answer-input-0']").send_keys(ans1)
        print "First Answer entered "
        print "Entering Second answer"
        driver.find_element_by_xpath(".//*[@id='question-answer-input-1']").send_keys(ans2)
        print "Second Answer entered "
        
        

         
        
        print "\nVerifying All the data entered is displaying in fields"
        
        if questionArea.text==questionCard:
            print "Question ::"+questionCard
        else:
            print "Question is not displayed"
            raise Exception
        
        
        if driver.find_element_by_xpath(".//*[@id='question-answer-input-0']").text==ans1:
            print "Answer 1 ::"+ans1
        else:
            print "Answer 1 is not displayed"
            raise Exception
        
        if driver.find_element_by_xpath(".//*[@id='question-answer-input-1']").text==ans2:
            print "Answer 2 ::"+ans2
        else:
            print "Answer 2 is not displayed"
            raise Exception


