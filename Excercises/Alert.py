from selenium import webdriver


class Alert:
    driver = webdriver.Chrome(executable_path="C:\\Users\\Varun\\Downloads\\Python\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.find_element_by_xpath("//input[@id='name']").send_keys("Varun")
    driver.find_element_by_id("alertbtn").click()
    alert_1 = driver.switch_to.alert
    print(alert_1.text)
    alert_1.accept()

    driver.find_element_by_id("confirmbtn").click()
    alert_1.dismiss()


Alert()
