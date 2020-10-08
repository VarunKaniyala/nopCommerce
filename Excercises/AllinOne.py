import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AllinOne:
    driver = webdriver.Chrome(executable_path="C:\\Users\\Varun\\Downloads\\Python\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.implicitly_wait(20)
    driver.maximize_window()

    # To move the mouse cursor
    act = ActionChains(driver)
    act.move_to_element(driver.find_element_by_xpath("//a[text()='Flight Booking']")).click().perform()

    # To move the vertical scroll bar
    driver.switch_to.window(driver.window_handles[1])
    driver.execute_script("window.scrollBy(0,700)")

    # Explict wait use
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[contains(text(),'Book Cab')]")))

    driver.find_element_by_xpath("//span[contains(text(),'Book Cab')]").click()  # Click on Book Cab related link
    time.sleep(10)  # Wait for 5 sec

    driver.close()  # Close only the current window
    driver.switch_to.window(driver.window_handles[0])  # Switch back to the previous window
    print(driver.current_url)  # Print the current URL


    # Switch to Alert for JavaScript Pop up
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.find_element_by_xpath("//input[@id='name']").send_keys("Varun")
    driver.find_element_by_id("alertbtn").click()
    alert_1 = driver.switch_to.alert
    print(alert_1.text)
    alert_1.accept()


AllinOne()
