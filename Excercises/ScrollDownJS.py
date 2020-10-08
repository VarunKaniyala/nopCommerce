from selenium import webdriver


class ScrollDownJS:
    driver = webdriver.Chrome(executable_path="C:\\Users\\Varun\\Downloads\\Python\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.implicitly_wait(20)
    driver.maximize_window()

    driver.execute_script("window.scrollBy(0,1000)")


ScrollDownJS()

