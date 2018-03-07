'''
Created on 05-Mar-2018

@author: Sheethu C
'''
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd
from BaseTestClass import driver


class Delete_Tags_Attributes_Lessons:
    
    def delete_Tag(self):
        
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div/section[2]/div/ul/li[1]/a")))
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/section[2]/div/ul/li[1]/a").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/header/div/button")))
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/header/div/button").click()
        print "Clicked on Delete Button"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div/button[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[2]/div/div/div[2]/div/button[1]")))
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div/button[1]").click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[2]/div/div")))
        time.sleep(3)
        
    def deleteLesson(self):
        
        print "\n\nDeleting all lessons.........."
        wait=WebDriverWait(driver, 80)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/lessons']")))
    
        print "Clicking on Lessons button from side menu"
        driver.find_element_by_xpath("//a[@href='/create/lessons']").click()
    
    def deleteItLesson(self):    
        wait=WebDriverWait(driver, 80)
        #wait.until(EC.visibility_of_element_located((By.XPATH,"//tr[1]/td[4]/button[.='Delete']")))
        
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.XPATH,"//tr[1]/td[4]/button[.='Delete']")))
        driver.find_element_by_xpath("//tr[1]/td[4]/button[.='Delete']").click()
        delo=wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[2]/button[1]")))
        delo.click()
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[2]/div/div/span")))     
    
    
    def deleteAttribute(self):
        
        wait=WebDriverWait(driver, 60)
        driver.find_element_by_xpath("//tr[1]/td[5]/button[.='Delete']").click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[2]/button[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[2]/div/div/div[2]/div[2]/button[1]")))
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[2]/button[1]").click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[2]/div/div")))
        time.sleep(3)
     
                
    def mainDeletetag(self):
        try:
            d=Delete_Tags_Attributes_Lessons()
            wait=WebDriverWait(driver, 80)
            wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a")))
            driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a").click()
            print "Clicked on admin icon"
            wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]")))
            driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]").click()
            print "Clicked on Admin"
            driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[5]").click()
            print "Clicked on Tag"
            
            ele=driver.find_elements_by_xpath("//li[@class='u-inline-block']/a")
            count=len(ele)
            print count
            
            if count==0:
                print "No Tags to delete"
            else: 
                wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div/section[2]/div/ul/li[1]/a")))
                print "Tag Page Loaded"
                
                for count in range (0,count):
                    d.delete_Tag()
                print "All Tags are deleted"   
        finally:
            book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url) 
            
    def mainDelete_attribute(self):
        try:    
            d=Delete_Tags_Attributes_Lessons()
            wait=WebDriverWait(driver, 60)
            wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a")))
            driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a").click()
            print "Clicked on admin icon"
            wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]")))
            driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]").click()
            print "Clicked on Admin"
            driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[1]").click()
            print "Clicked on User Attribute"
            driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[4]").click()
            print "User attribute Page Loaded"
           
            wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div/div/div[2]/div/table/tbody/tr[1]/td[5]/button")))
            print "Deleting all attributes"
            ele=driver.find_elements_by_xpath("//tbody/tr/td[5]/button")
            count=len(ele)
            print count
            
            for count in range (0,count):
                d.deleteAttribute()
            print "All Attributes are deleted"  
            
        finally:
            book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url) 

            
    def mainDeleteLessons(self):
        try:
            d=Delete_Tags_Attributes_Lessons()
            d.deleteLesson()
            wait=WebDriverWait(driver, 60)
            wait.until(EC.visibility_of_element_located((By.XPATH,"//tr[1]/td[4]/button[.='Delete']")))
            ele=driver.find_elements_by_xpath("//tbody/tr/td[4]/button[.='Delete']")
            count=len(ele)
            print count
            
            if count==0:
                print "No Lessons to delete"
            else: 
                for count in range (0,count):
                    d.deleteItLesson()
                print "All Lessons are deleted" 
            
        finally:
            book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url) 
     
    def mainDeleteAll(self):
        try:     
            d=Delete_Tags_Attributes_Lessons()
            d.mainDeletetag()
            d.mainDelete_attribute()
            d.mainDeleteLessons()
            
        finally:
            book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)            
                
       
         
    