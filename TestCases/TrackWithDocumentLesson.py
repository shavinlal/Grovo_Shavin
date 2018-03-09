'''
Created on 23-Feb-2018

@author: QA
'''
import os.path
import time
import traceback
from BaseTestClass import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

class TrackWithDocumentLesson:
    
    def lessonWithDocument(self,lessonname,documentPath,timeToUploaddocument):
        
        wait=WebDriverWait(driver, timeToUploaddocument)
        
        print "This is lesson with document"
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/lessons']")))
        
        print "Clicking on Lessons button from side menu"
        driver.find_element_by_xpath("//a[@href='/create/lessons']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div/button")))
     
        print "Click on Create lesson button"
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/header/div/button").click()
        
        print "Verifying Create new lesson tab is displayed"
        
        #assert "Create a new lesson"==driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/h3").text
        if driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/h3").text == "Create a new lesson":
            print("Create a new lesson tab is displayed")
        else:
            print ""
            raise Exception
        
        # self.assertEqual("Create a new lesson", driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/h3").text)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[2]/div")))

        print "Clicked on Blank lesson"
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[2]/div").click()
        
        print "Creating New lesson With one Text card"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea")))

        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").send_keys(lessonname)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']")))
        
        print "Entered lesson name ::"+lessonname
        
        print "Click on (+) icon"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div/span").click()
        
        #Clicking on Document card
        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[4]/div[1]/div").click()
        
        time.sleep(4)
        
        #Uploading Document
        print "Uploading Document"
        driver.find_element_by_css_selector('input[type="file"]').send_keys(documentPath)
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='content']/div/div/div[3]/div[2]/div/div/div[1]/div/a")))
        
        documentContainerlocator_afterupload= driver.find_element_by_xpath("//*[@id='content']/div/div/div[3]/div[2]/div/div/div[1]/div/a")
        
        if(documentContainerlocator_afterupload.is_displayed()):
            
            print "Successfully uploaded the Video file"
            
        else:
            print "Failed to upload the Document file"
            raise Exception
        
        print "Publishing lesson"
        publishButton=wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button")))
        publishButton.click()

        wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]")))
        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]").click()
        print "Clicked on publish button"
        
        # verifying success message
        
        print "Verifying Success message"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[2]/div/div/span[2]")))

        headerText=driver.find_element_by_xpath(".//*[@id='content']/div/div/div[2]/div/div/span[2]").text
        print "Message '"+headerText+"' is displayed"
        
        if "You have successfully published" in headerText:
            print("Create a new lesson tab is displayed")
        else:
            print "Success message is not displayed"
            raise Exception

        print "Lesson published"
        
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[1]/a").click()
        
        #Verifying created lesson is displayed in list
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td[2]/a[.='"+lessonname+"'])[1]")))

        if driver.find_element_by_xpath("(//tbody/tr/td[2]/a[.='"+lessonname+"'])[1]").is_displayed():
            
            print "Lesson is displayed in Grid ::"+lessonname
            
        else:
            print "Lesson not displaying in grid"
            raise Exception
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[4]").click()

    def createTrackwithDocument(self,titleOfTrack,Imagefilepath,description,tagName,lessonname,expectedSuccessText):
        print "Creating track with one lesson contains Text Card"
        
        wait=WebDriverWait(driver, 120)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/lessons']")))
        
        print "Clicking on Lessons button from side menu"
        driver.find_element_by_xpath("//a[@href='/create/lessons']").click()
        
        print "Clicking on Track button from side menu"
        driver.find_element_by_xpath("//a[@href='/create/tracks']").click()
        
        createTrackbutton=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div/a")))
        
        createTrackbutton.click()
        
        print "Entering title"
        titlefield=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='title']")))
        titlefield.send_keys(titleOfTrack)
        print "Title entered ::"+titleOfTrack
        
        driver.find_element_by_css_selector('input[type="file"]').send_keys(Imagefilepath)
        print "waiting to upload image"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/img")))
        print "Image uploaded"
        
        print "Entering Description"
        driver.find_element_by_xpath(".//*[@id='description']").send_keys(description)
        print "Description entered ::"+description 
        
        
        print "Adding tag"
        addTags=driver.find_element_by_xpath("//div[@class='Select-placeholder']")
        webdriver.ActionChains(driver).move_to_element(addTags).click().send_keys(tagName).perform()
        
        option=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='react-select-2--option-0']")))
        webdriver.ActionChains(driver).move_to_element(option).click(option).perform()
        
        driver.find_element_by_xpath(".//*[@id='description']").send_keys(" ")
        
        
        print "Adding created lesson"
        
        print "Clicking on Add lessons button"
       
        driver.execute_script("window.scrollTo(0, 0);")
        addlessonbutton=driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div/button")
        addlessonbutton.click()
       
       
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[2]/div/ul/li[1]/div[1]/div")))
        
        print "Searching for lesson in Add lessons pop up"
        driver.find_element_by_xpath(".//*[@id='search-lessons-in-modal']").send_keys(lessonname)
        
        searchedLesson=wait.until(EC.visibility_of_element_located((By.XPATH,"//li/div[2]/h4[.='"+lessonname+"']/../../div[1]/div")))
        searchedLesson.click()
        
        print "Lesson '"+lessonname+"' selected"
        print "Adding to Track"
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[3]/button[1]").click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div/ul/li/div[2]/div/h4/div")))
        
        print "Checking added lesson is selected lesson from Pop up"
        lessonTextAddedToGrid=driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div/ul/li/div[2]/div/h4/div").text

        if lessonTextAddedToGrid==lessonname:
            print "Selected Lesson is displayed in grid of tracks page"
        
        else:
            print "Lesson is not displayed"
            raise Exception
        
        print "Clicking on Publish Track button"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/div/div[2]/div[2]/div[3]/button").click()
        
        print "Verifying Success message is displaying"
        
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[2]/div/div/span")))
        actualSuccessText=driver.find_element_by_xpath(".//*[@id='content']/div/div[2]/div/div/span").text
        
        if actualSuccessText==expectedSuccessText:
            print "Success message '"+actualSuccessText+"' is displayed"
        else:
            print "failed to display expected success message"
            raise Exception
        
        
        print "Verifying Creates track '"+titleOfTrack+"' is displayed in Tracks grid"
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[2]/div[3]/div/ul/li[2]/a").click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr/td[2]/a[.='"+titleOfTrack+"']")))
        
        trackInGrid=driver.find_element_by_xpath("//tbody/tr/td[2]/a[.='"+titleOfTrack+"']").text
        
        if trackInGrid==titleOfTrack:
            print "Track '"+trackInGrid+"' is displayed in grid"
        else:
            print "Track is not displayed in grid"
            raise Exception
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[4]").click()
        
       
    def lessonWithDocumentCard(self):
        
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('TrackCreate')
        
        cell1 = first_sheet.cell(34,1)
        titleOfTrack = cell1.value
        
        cell2 = first_sheet.cell(35,1)
        Imagefilepath = cell2.value
        
        print "Image file path"
        print Imagefilepath 
        
        cell2 = first_sheet.cell(36,1)
        description = cell2.value
        
        cell2 = first_sheet.cell(37,1)
        tagName = cell2.value
        
        cell2 = first_sheet.cell(34,3)
        lessonname= cell2.value
        
      
        cell2 = first_sheet.cell(38,1)
        expectedSuccessText= cell2.value
        
       
        cell2 = first_sheet.cell(35,3)
        documentPath = cell2.value
        
        print "Document file path"
        print documentPath 
        
        cell2 = first_sheet.cell(36,3)
        timeToUploaddocument = cell2.value
        
        try:     
            doc=TrackWithDocumentLesson()
            doc.lessonWithDocument(lessonname, documentPath, timeToUploaddocument)
            doc.createTrackwithDocument(titleOfTrack, Imagefilepath, description, tagName, lessonname, expectedSuccessText)
        
        except Exception as e:
            traceback.print_exc()
            print (e)
            raise Exception
        
        finally:   
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)
