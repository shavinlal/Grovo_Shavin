'''
Created on 23-Feb-2018

@author: dattatraya
'''

import os
import time
import traceback

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd


class DeleteLesson:
   
    def deleteIt(self):    
        wait=WebDriverWait(driver, 60)
        #wait.until(EC.visibility_of_element_located((By.XPATH,"//tr[1]/td[4]/button[.='Delete']")))
        
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td[.='Published']/../td[4]/button[3])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,"(//tbody/tr/td[.='Published']/../td[4]/button[3])[1]")))
        driver.find_element_by_xpath("(//tbody/tr/td[.='Published']/../td[4]/button[3])[1]").click()
        delo=wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[2]/button[1]")))
        delo.click()
        wait.until(EC.invisibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[1]/button")))
        
        
    def mainDelete(self):
        try:
            d=DeleteLesson()
            print "\n\nDeleting all lessons.........."
            wait=WebDriverWait(driver, 60)
            wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/lessons']")))
        
            print "Clicking on Lessons button from side menu"
            driver.find_element_by_xpath("//a[@href='/create/lessons']").click()
            
            
            wait=WebDriverWait(driver, 60)
            wait.until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr/td[.='Published']/../td[4]/button[3]")))
            ele=driver.find_elements_by_xpath("//tbody/tr/td[.='Published']/../td[4]/button[3]")
            print "Deleting Lesson"
            count=len(ele)
            
            for count in range (0,count):
                d.deleteIt()
            
            print "All Elements are deleted"
            
        except Exception as e:
            traceback.print_exc()
            print (e)
            raise Exception 
        finally:
            book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)


        
        
        
        