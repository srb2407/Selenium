import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    ser_obj = Service()
    driver_options = Options()
    driver_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=ser_obj, options=driver_options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    request.cls.driver = driver

    yield driver
    driver.close()
