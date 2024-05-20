from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager 
import time 

# Example 1 - Simple

# load website 
url = 'https://angular.io/' 

# instantiate options
#driver_exe = 'chromedriver'
options = Options()

# run browser in headless mode 
options.add_argument("--headless")
#driver = webdriver.Chrome(driver_exe, options=options)
 
 
# instantiate driver 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install()), options=options) 

 
driver.get(url) 
 
print(driver.page_source)


# Example 2 - Search by Tag

# instantiate options
#driver_exe = 'chromedriver'
options = Options()

# run browser in headless mode 
options.add_argument("--headless")
#driver = webdriver.Chrome(driver_exe, options=options)
 
 
# instantiate driver 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install()), options=options) 
 
# get the entire website content 
driver.get(url) 
 
# select elements by class name 
elements = driver.find_elements(By.CLASS_NAME, 'text-container') 
for title in elements: 
	# select H2s, within element, by tag name 
	heading = title.find_element(By.TAG_NAME, 'h2').text 
	# print H2s 
	print(heading)


# Example 3 - Complete Search
#driver_exe = 'chromedriver'
options = Options()

# run browser in headless mode 
options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) 
 
# load target website 
url = 'https://scrapingclub.com/exercise/list_infinite_scroll/' 
 
# get website content 
driver.get(url) 
 
# instantiate items 
items = [] 
 
# instantiate height of webpage 
last_height = driver.execute_script('return document.body.scrollHeight') 
 
# set target count 
itemTargetCount = 20 
 
# scroll to bottom of webpage 
while itemTargetCount > len(items): 
	driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') 
 
	# wait for content to load 
	time.sleep(1) 
 
	new_height = driver.execute_script('return document.body.scrollHeight') 
 
	if new_height == last_height: 
		break 
 
	last_height == new_height 
 
	# select elements by XPath 
	elements = driver.find_elements(By.XPATH, "//div/h4/a") 
	h4_texts = [element.text for element in elements] 
 
	items.extend(h4_texts) 
 
	# print title 
	print(h4_texts)


