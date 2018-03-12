'''
Created on 07-Mar-2018

@author: geethukn
'''
from operator import contains
import os.path

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait, expected_conditions as EC
from selenium.webdriver.support.select import Select
import xlrd

from BaseTestClass import BaseTestClass
from BaseTestClass import WebDriverWait
from BaseTestClass import driver


class BasicInfoPasswordCreation_35:
    
    def testPasswordCreationForUser(self):
        print "Reading data from excel sheet"
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        sheet1=book.sheet_by_name('API testing')
        print("Fetching the LastName from Excel to search")
        #Read from Excel to search
        cell1 = sheet1.cell(4,1)
        searchlastName = cell1.value
        #Clicking on Admin Menu from Grovo Application
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a").click()
        wait=WebDriverWait(driver,80)
        wait.until(EC.visibility_of_element_located((By.ID,"search-users")))
        driver.find_element_by_id("search-users").send_keys(searchlastName)
        #To click on FirstName link
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div/div[4]/table/tbody/tr[1]")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/div/div[4]/table/tbody/tr/td[1]/a").click()
        #To verify FirstName field 
        print"Verify FirstName field"
        wait.until(EC.visibility_of_element_located((By.ID,"create-edit-user-search-firstName")))
        firstNamelocator=driver.find_element_by_id("create-edit-user-search-firstName")
        firstName =firstNamelocator.get_attribute("value") 
        if not firstName:
            print"FirstName field is empty"
        else:
            print"FirstName is present :" +firstName
        #To verify LastName field 
        print"Verify LastName field"  
        lastNamelocator =driver.find_element_by_id("create-edit-user-search-lastName")
        lastName=lastNamelocator.get_attribute("value")
        if not lastName:
            print"LastName field is empty"
        else:
            print"LastName is present : "+lastName
        #To verify Email field 
        print"Verify Email field"
        emaillocator =driver.find_element_by_id("create-edit-user-search-username")
        global email
        email =emaillocator.get_attribute("value")
        if not email:
            print"Email field is empty"
        else:
            print"Email is present : "+email
        #To verify Employee ID field 
        print"Verify Employee ID field"
        employeeidlocator =driver.find_element_by_id("create-edit-user-search-employeeId")
        employeeid=employeeidlocator.get_attribute("value")
        if not employeeid:
            print"Employee ID field is empty"
        else:
            print"Employee ID is present : "+employeeid
        #To verify Direct Roles field 
        print"Verify Direct Roles field"  
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//span[@role='option'])[1]")))
        DirectRoleslocator =driver.find_element_by_xpath("(//span[@role='option'])[1]")
        DirectRoles=DirectRoleslocator.text
        if not DirectRoles:
            print"Direct Roles field is empty"
        else:
            print"Direct Roles is present : "+DirectRoles
        #LogOut function      
        driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/div/nav/div[2]/a/span[3]").click()
        print "Clicked on SignOut Dropdown"
        driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/div[2]/div[2]/a").click()
        print "Clicked on signOut Button"
        wait.until(EC.visibility_of_element_located((By.ID,"username")))
    def Logincreateuser(self):    
        print "Reading data from excel sheet"
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        sheet1=book.sheet_by_name('API testing')
        cell2 = sheet1.cell(4,2)
        Currentpassword = cell2.value
        cell3 = sheet1.cell(4,3)
        Newpassword = cell3.value
        wait=WebDriverWait(driver, 80)
        print "Grovo Sign-In page is displayed"
        print "Enter User name"
        driver.find_element_by_id("username").send_keys(email) 
        print "Enter Password"
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
        element.send_keys(Currentpassword)
        element.send_keys(Keys.TAB)
        print "Clicking on Sign_In button"
        driver.find_element_by_xpath("//*[@id='submitButton']").click()
        wait.until(EC.visibility_of_element_located((By.ID,"currentPassword")))
        driver.find_element_by_id("currentPassword").send_keys(Currentpassword)
        print "Current Password is entered :"+Currentpassword
        driver.find_element_by_id("newPassword").send_keys(Newpassword)
        print "New Password is entered :"+Newpassword
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[1]/div[2]/button")))
        wait.until(EC.visibility_of_element_located((By.ID,"global-header-search")))
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[1]/div[2]/button").click()
        Home=driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[1]")
        Library = driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[2]")
        Create = driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[3]")
        Campaign = driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[4]")
        if(Home.is_displayed() and Library.is_displayed() and Create.is_displayed() and Campaign.is_displayed()):
            print "User with Creator Role is able to login and HOME,LIBRARY,CREATE and CAMPAIGN is displaying.."
        else:
            print"Home page not displayed"
            raise Exception
            print Exception
        print "Sign out "
        ele =driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/div[1]/nav/div[2]/a/span[3]")
        driver.execute_script('arguments[0].click()',ele)
        elem=driver.find_element_by_xpath("html/body/div/div/div[1]/div[2]/div[2]/a")
        driver.execute_script('arguments[0].click()',elem)
        
    def BasicInformationWithDirectRole(self):
        try:
            obj=BasicInfoPasswordCreation_35()
            obj.testPasswordCreationForUser()
            obj.Logincreateuser()  
        finally:
            book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)