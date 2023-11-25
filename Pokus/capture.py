from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import os
import time
from urllib.parse import urlparse, urljoin
from selenium.webdriver.common.by import By
import cssbeautifier
import csscompressor

def get_css(driver, url):
    css_content = []
    links = driver.find_elements(By.CSS_SELECTOR, "link[rel='stylesheet']")
    for link in links:
        css_url = link.get_attribute('href')
        absolute_css_url = urljoin(url, css_url)
        try:
            response = requests.get(absolute_css_url)
            if response.status_code == 200:
                compressed_css = csscompressor.compress(response.text)
                beautified_css = cssbeautifier.beautify(compressed_css)
                css_content.append(beautified_css)
        except requests.RequestException as e:
            print(f"Error downloading {absolute_css_url}: {e}")
    return css_content

def parse_html_classes_ids(html):
    soup = BeautifulSoup(html, 'html.parser')
    all_classes_ids = set()
    for element in soup.find_all(True):
        if element.get('class'):
            all_classes_ids.update(element.get('class'))
        if element.get('id'):
            all_classes_ids.add(element.get('id'))
    return all_classes_ids

def filter_css(css_text, html_classes_ids):
    filtered_css = []
    for rule in css_text.split('}'):
        if any(html_class in rule for html_class in html_classes_ids):
            filtered_css.append(rule + '}')
    return '\n'.join(filtered_css)

def truncate_css(css_content, max_rules=200):
    """ Truncate the CSS content to a specified number of rules. """
    rules = css_content.split('}')
    truncated = '}'.join(rules[:max_rules]) + '}'
    return truncated

# URL to visit
url = 'http://banmi.marekhorvath.sk/'

# Set up WebDriver options for headless mode
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# Set up WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Go to the URL
driver.get(url)

# Wait for the page to fully load
time.sleep(5)

# Get HTML source and beautify it
html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')
pretty_html = soup.prettify()

# Parse HTML for classes and IDs
classes_ids = parse_html_classes_ids(html_source)

# Get CSS and filter it based on the HTML classes/IDs, then truncate
css_files = get_css(driver, url)
filtered_css_content = [filter_css(css, classes_ids) for css in css_files]
truncated_css_content = [truncate_css(css) for css in filtered_css_content]

# Save HTML and CSS
domain_name = urlparse(url).netloc
html_file_path = os.path.join(os.getcwd(), f'{domain_name}_source.html')
css_file_path = os.path.join(os.getcwd(), f'{domain_name}_styles.css')

with open(html_file_path, 'w', encoding='utf-8') as file:
    file.write(pretty_html)

with open(css_file_path, 'w', encoding='utf-8') as file:
    for css in truncated_css_content:
        file.write(css + '\n\n')

# Close the browser
driver.quit()

print(f"HTML saved as {html_file_path}")
print(f"CSS saved as {css_file_path}")
