from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# create a new Firefox session
driver=webdriver.Chrome("TestCases/chromedriver")
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get("https://optislabs-playpen.grovo.com/")

# close the browser window
driver.quit()
