from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
import time

def accept_cookies(driver):
    try:
        # Wait for the cookie popup to be visible and find the accept button
        accept_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept')]"))
        )
        accept_button.click()
    except Exception as e:
        print("No cookie popup found or accept button not clicked.", e)

def get_full_page_screenshot(driver, file_name):
    # Scroll to the bottom of the page to calculate full page height
    total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
    
    # Set the window size to capture the full page
    driver.set_window_size(1920, total_height)  # Width can be adjusted as needed
    
    # Take full page screenshot
    driver.get_screenshot_as_file(file_name)

# URL to visit
url = 'http://banmi.marekhorvath.sk/'

# Extract top-level domain for screenshot name
domain_name = urlparse(url).netloc.split('.')[-2]

# Set up WebDriver options for headless mode
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Necessary for headless mode on Windows

# Set up WebDriver (this example uses Chrome)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Go to the URL
driver.get(url)

# Try to accept cookies
accept_cookies(driver)

# Wait for the page to fully load
time.sleep(5)

# Take full page screenshot and save it
screenshot_path = f'{domain_name}.png'
get_full_page_screenshot(driver, screenshot_path)

# Close the browser
driver.quit()

print(f"Screenshot saved as {screenshot_path}")
