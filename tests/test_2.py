from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestSort:
    def testDataSorting(self):
        ser_obj = Service()
        driver_options = Options()
        driver_options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(service=ser_obj, options=driver_options)
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        driver.find_element(By.ID, 'login-button').click()
        sort_options = Select((driver.find_element(By.XPATH, "//select[@class='product_sort_container']")))
        sort_options.select_by_visible_text('Price (low to high)')

        item_list = driver.find_elements(By.XPATH, "//div[@class='inventory_item_price']")
        prices = []
        for i in item_list:
            price = i.text.split('$')[1]
            prices.append(float(price))
        sorted_list = sorted(prices, reverse=True)

        try:
            assert prices == sorted_list
        except AssertionError as SortError:
            print('Sort Failed')
