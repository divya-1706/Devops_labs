from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
print("Continuous XPath Search Demo Starting...")
driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(3)
search_terms = [
"XPath examples",
"Selenium XPath tutorial",
"XPath contains example"
]
for term in search_terms:
    print(f" Searching for: {term}")
    # Always re-find element fresh (important)
    search = driver.find_element(By.NAME, "q")
    # Clear properly
    search.clear()
    time.sleep(1)
    # Type slowly (avoid bot detection)
    for char in term:
        search.send_keys(char)
        time.sleep(0.1)
    time.sleep(1)
    search.send_keys(Keys.RETURN)
    print("Search executed")
    time.sleep(5)
# Go back to Google homepage (IMPORTANT FIX)
    driver.get("https://www.google.com")
    time.sleep(3)
input("Press ENTER to close browser...")
driver.quit()