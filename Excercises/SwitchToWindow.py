from selenium import webdriver


class SwitchToWindow:
    driver = webdriver.Chrome(executable_path='C:\\Users\\Varun\\Downloads\\Python\\chromedriver.exe')
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.implicitly_wait(10)

    driver.find_element_by_xpath("//a[text()='Click Here']").click()
    a = driver.window_handles[1]
    driver.switch_to.window(a)
    print(driver.find_element_by_tag_name("h3").text)


SwitchToWindow()