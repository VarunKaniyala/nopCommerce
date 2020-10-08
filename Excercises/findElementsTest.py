from selenium import webdriver


class FindElementsTest():

    driver = webdriver.Chrome(executable_path="C:\\Users\\Varun\\Downloads\\Python\\chromedriver.exe")
    driver.get("https://www.makemytrip.com/")
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.find_element_by_xpath("//input[@id='fromCity']").send_keys("Ind")
    from_list = driver.find_elements_by_xpath("//*[contains(@class,'react-autosuggest__input')]")
    for i in from_list:
        if i.text == "Delhi, India":
            i.click()
            pass
    print(driver.find_element_by_xpath("//input[@id='fromCity']").get_attribute("value"))
    driver.find_element_by_xpath("//*[contains(@id,'toCity')]").send_keys("Ban")
    to_list = driver.find_elements_by_xpath("//*[contains(@class,'hsw_autocomplePopup autoSuggestPlugin')]//div[1]//div[1]//div[1]")
    for x in to_list:
        print(x.text)
        if x.text in "Bengaluru":
            x.click()
            x.click()
            break
    print(driver.find_element_by_xpath("//*[contains(@id,'toCity')]").get_attribute("value"))
    assert driver.find_element_by_xpath("//*[contains(@id,'toCity')]").get_attribute("value") == "Bangalore"
    #driver.close()


FindElementsTest()
