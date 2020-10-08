import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Shop_EndToEnd:
    driver = webdriver.Chrome(executable_path="C:\\Users\\Varun\\Downloads\\Python\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(20)
    driver.maximize_window()
    driver.find_element_by_xpath("//a[text()='Shop']").click()

    # Get the product name
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.execute_script("window.scrollBy(0,1000)")
    wait = WebDriverWait(driver, 20)
    wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//button")))
    a = driver.find_elements_by_xpath("//div[@class='card h-100']")

    # wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, '//button//parent::div/parent::div//h4')))
    y = []
    for i in a:
        x = i.find_element_by_xpath("div/h4/a")
        print(x.text)
        if x.text == "iphone X":
            y.append(i.find_element_by_xpath("div/h4/a").text)
            i.find_element_by_xpath("div/button").click()
            break

    driver.find_element_by_xpath("//li[@class='nav-item active']").click()
    z = driver.find_element_by_xpath("//h4/a")  # Checkout page confirmation
    print(z.text)

    if y[0] == z.text:
        print("Correct product checkout")
    else:
        print("Wrong checkout")

    driver.find_element_by_xpath("//tbody/tr[3]/td[5]/button[1]").click()
    driver.find_element_by_xpath("//input[@id='country']").send_keys("rahulshettyacademy")
    time.sleep(3)
    driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']/label").click()
    time.sleep(3)
    driver.find_element_by_xpath("//input[@type='submit']").click()

    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[contains(@class,'alert-success')]")))
    message = driver.find_element_by_xpath("//div[contains(@class,'alert-success')]").text
    print(message)
    driver.get_screenshot_as_file("Success_Image.png")

    driver.close()


Shop_EndToEnd()
