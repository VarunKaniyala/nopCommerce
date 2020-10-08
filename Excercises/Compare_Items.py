from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Compare_Items:
    driver = webdriver.Chrome(executable_path="C:\\Users\\Varun\\Downloads\\Python\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.implicitly_wait(10)
    driver.maximize_window()

    # Enter "C" in Search Box
    driver.find_element_by_xpath("//input[@type='search']").send_keys("C")
    # wait till the item names are loaded and keep all names as web elements in variable items1
    # iterate to get the names from web elements
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.product h4')))
    items1 = driver.find_elements_by_css_selector(".product h4")
    print(len(items1))
    li_1 = []
    for i in items1:
        li_1.append(i.text)

    print(li_1)

    # Adding count of each items
    AddItem = driver.find_elements_by_xpath("//a[text()='+']")
    for j in AddItem:
        j.click()

    # Adding each selected items to cart using button "ADD TO CART"
    AddCart = driver.find_elements_by_css_selector(".product-action button")
    for k in AddCart:
        k.click()

    # Click on cartoon bag image to confirm & proceed to checkout
    driver.find_element_by_css_selector(".cart-icon").click()
    driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

    # wait till the next page with items table loads and then fetch all item names in to a list
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//td[2]/p')))
    items2 = driver.find_elements_by_xpath("//td[2]/p")
    li_2 = []
    for l in items2:
        li_2.append(l.text)
    print(li_2)

    # compare both the lists
    if li_1 == li_2:
        print("Lists are same")
    else:
        print("Lists are not same")
    driver.close()


Compare_Items()
