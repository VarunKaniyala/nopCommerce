import time

from selenium import webdriver
import keyboard
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class IframeHandle:
    driver = webdriver.Chrome(executable_path="C:\\Users\\Varun\\Downloads\\Python\\chromedriver.exe")
    driver.get("https://the-internet.herokuapp.com/iframe")
    driver.implicitly_wait(20)
    driver.maximize_window()
    driver.switch_to.frame("mce_0_ifr")
    a = driver.find_element_by_xpath("//p")
    print(a.text)
    a.send_keys(Keys.CLEAR)
    a.send_keys("Hi I'm here")
    # driver.switch_to_default.content()
    driver.close()
    #To clear the content in the text field
    # for i in range(0, 23):
    #     print(a)
    #     a.send_keys(Keys.BACK_SPACE)
    #
    # a.send_keys("ABC")
    # driver.switch_to_default.content()
    # driver.close()


IframeHandle()
