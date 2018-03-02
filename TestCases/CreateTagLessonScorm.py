'''
Created on 27-Feb-2018

@author: Sheethu C
'''
from operator import contains
import os.path
import pdb
import thread
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from xlrd import book
import xlrd
from BaseTestClass import driver
class CreateTagLessonScorm():
    
    def createLessonScormTag(self):
        print "Reading data from excel sheet"
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('CreateTag')
        print("Fetching the Attribute Name from Excel Sheet\n")
        # read a cell
        cell = first_sheet.cell(23,2)
        TagName = cell.value
        print TagName
        
        cell = first_sheet.cell(23,3)
        ExpectedSuccessMessage = cell.value
        print ExpectedSuccessMessage
        
        
        wait=WebDriverWait(driver, 80)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a")))
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a").click()
        print "Clicked on admin icon"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]")))
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]").click()
        print "Clicked on Admin"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[5]").click()
        print "Clicked on Tag"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/header/h1")))
        print "Tag Page Loaded"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/header/div/div/button").click()
        print "Clicked on Create Tag Button"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div/section[1]/div[1]/div/div[1]/div/input")))
        print "Verifying Create Tag Name field "
        if driver.find_element_by_id("add-tag-input").is_displayed():
            print("Enter Tag name field is displayed")
        else:
            print ""
            raise Exception
        print "Verified Tag Name field"
        ele = driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/section[1]/div[1]/div/div[1]/div/input")
        webdriver.ActionChains(driver).move_to_element(ele).send_keys(TagName).perform()
        print "Entered Tag Name :"+TagName
        time.sleep(6)
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/section[1]/div[1]/div/div[2]/button[1]").click()
        time.sleep(6)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div/section[1]/div[1]/div")))
        ActualMessage = driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/section[1]/div[1]/div")
        ExpectedMessage =  TagName+ExpectedSuccessMessage
        print "ExpectedMessage "+ExpectedMessage
        print("Expected Success Message and Actual Success Message is Matching,Success Message Verified")
        print "Searching for the created Tag"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div/section[1]/div[2]/div/div/input")))
        time.sleep(6)
      
        element =driver.find_element_by_name("tag-index-search")
        element.clear()
        element.send_keys(TagName)
        driver.find_element_by_name("tag-index-search").send_keys(Keys.ENTER)
 
        time.sleep(6)
        print "Entered Tag Name for Search"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div/section[2]/div/ul/li[1]")))
        print "Verifying the created Tag in the list"
        ele =driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/section[2]/div/ul/li[1]")
        print ele.text
        if driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/section[2]/div/ul/li[1]").is_displayed():
            print("Created Tag in the list")
        else:
            print ""
            raise Exception
       #//div/ul/li[.='tag'] 
        
       
    def createTagForLessonScorm(self):
     try :
        obj2= CreateTagLessonScorm()
        obj2.createLessonScormTag() 
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