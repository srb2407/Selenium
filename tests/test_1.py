import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:
    @pytest.mark.xfail
    def testLoginUsers(self):
        ser_obj = Service()
        driver_options = Options()
        driver_options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(service=ser_obj, options=driver_options)
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(driver, 10)

        user = driver.find_element(By.ID, 'user-name')
        user.clear()
        user.send_keys()
        passw = driver.find_element(By.ID, 'password')
        passw.clear()
        passw.send_keys()
        driver.find_element(By.ID, 'login-button').click()
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        logout = wait.until(EC.element_to_be_clickable(driver.find_element(By.ID, "logout_sidebar_link")))
        logout.click()
        driver.quit()
