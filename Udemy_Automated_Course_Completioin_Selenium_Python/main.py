from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("courseHomeURL")

elem = driver.find_element_by_id("email--1")
elem.send_keys("email")
elem = driver.find_element_by_id("id_password")
elem.send_keys("password")
elem = driver.find_element_by_id("submit-id-submit")
elem.send_keys(Keys.RETURN)

containers = driver.find_elements_by_class_name("section--section--BukKG")

print(containers)
for items in containers:
    items.click()
    print("Clicking")

containers =  driver.find_elements_by_xpath("//label[@class='curriculum-item-link--progress-toggle--1CMcg checkbox-inline']")
for item in containers:
    item.click()
    print("Clicking")
containers = driver.find_elements_by_css_selector("[data-purpose: \"progress-toggle-button\"]")
