import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Shop_veg:

    driver = webdriver.Chrome(executable_path="C:\\Users\\Varun\\Downloads\\Python\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.implicitly_wait(20)
    driver.maximize_window()

    driver.find_element_by_css_selector("input[type='search']").send_keys("ca")
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.product')))
    items = driver.find_elements_by_xpath("//button[text()='ADD TO CART']")
    print(len(items))
    for i in items:
        i.click()

    driver.find_element_by_xpath("//a[@class='cart-icon']").click()
    driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
    driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
    print(driver.find_element_by_xpath("//b[text()='Total After Discount : ']").text)
    print(driver.find_element_by_css_selector(".discountAmt").text)
    driver.find_element_by_css_selector("button.promoBtn").click()

    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[text()='Code applied ..!']")))
    print(driver.find_element_by_xpath("//b[text()='Total After Discount : ']").text)
    print(driver.find_element_by_css_selector(".discountAmt").text)
    driver.find_element_by_xpath("//button[text()='Place Order']").click()


Shop_veg()
