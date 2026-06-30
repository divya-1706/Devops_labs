from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
print("Starting Test...")
driver = webdriver.Chrome()
print("Opening Google...")
driver.get("https://www.google.com")
print("Locating search box...")
search = driver.find_element(By.NAME, "q")
print(" Typing 'MIT college'...")
search.send_keys("MIT college")
search.send_keys(Keys.RETURN)
print("Search executed successfully!")
input("Press ENTER to close the browser...")
print("Closing browser...")
driver.quit()
print("Test Completed!")