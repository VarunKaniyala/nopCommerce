from selenium import webdriver

class Locator_linkText():


    driver = webdriver.Chrome(executable_path="C:\\Users\\Varun\\Downloads\\Python\\chromedriver.exe")
    driver.get("https://login.salesforce.com/")
    driver.implicitly_wait(10)
    driver.find_element_by_link_text("Forgot Your Password?").click()
    driver.find_element_by_xpath("//input[@id='continue']").click()


Locator_linkText()
