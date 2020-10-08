import time

from selenium import webdriver
from selenium.webdriver.support.select import Select


class AutoSuggest:
    driver = webdriver.Chrome(executable_path="C:\\Users\\Varun\\Downloads\\Python\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
    driver.implicitly_wait(20)
    driver.find_element_by_xpath("//input[@id='ctl00_mainContent_ddl_originStation1_CTXT']").click()
    Lst = driver.find_elements_by_xpath("//div[@id='dropdownGroup1']/div[1]//li")

    for i in Lst:

        print(i.text)
        if i.text == "Bengaluru (BLR)":
            i.click()
            break
    # print(driver.find_element_by_xpath("//input[@id='autosuggest']").get_attribute('value'))

    driver.find_element_by_css_selector("input[id='ctl00_mainContent_ddl_destinationStation1_CTXT']").click()
    to_lst = driver.find_elements_by_xpath("//div[@id='dropdownGroup1']/div/ul/li")
    for j in to_lst:
        print(j.text)
        if j.text == "Kochi (COK)":
            j.click()
            break
    driver.find_element_by_xpath("//tbody/tr[5]/td[4]/a").click()
    currency = Select(driver.find_element_by_id("ctl00_mainContent_DropDownListCurrency"))
    currency.select_by_index(1)
    driver.find_element_by_xpath("//input[@id='ctl00_mainContent_btn_FindFlights']").click()


AutoSuggest()
