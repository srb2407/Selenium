import openpyxl
from pandas import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:
    def testLoginUsers(self):
        ser_obj = Service()
        driver_options = Options()
        driver_options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(service=ser_obj, options=driver_options)
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(driver, 10)

        xls = ExcelFile('login_cred.xlsx')
        df = xls.parse(xls.sheet_names[0])
        dictionary = df.to_dict()

        count = 0
        print(dictionary)
        #for key, value in dictionary.items():
            #self.loginLoop(driver, key, value)
            #count += 1
            #print(count)
            #driver.find_element(By.ID, "react-burger-menu-btn").click()
            #logout = wait.until(EC.element_to_be_clickable(driver.find_element(By.ID, "logout_sidebar_link")))
            #logout.click()

    #def loginLoop(self, driver, username, password):
        #user = driver.find_element(By.ID, 'user-name')
        #user.clear()
        #user.send_keys(username)
        #passw = driver.find_element(By.ID, 'password')
        #passw.clear()
        #passw.send_keys(password)
        #driver.find_element(By.ID, 'login-button').click()
