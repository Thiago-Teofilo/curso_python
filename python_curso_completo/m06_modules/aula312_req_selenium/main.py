from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

ROOT_FOLDER = Path(__file__).parent
CHROME_DRIVER = ROOT_FOLDER / 'drivers'/ 'chromedriver.exe'

WAIT_TIME = 20

chrome_options = webdriver.ChromeOptions()
chrome_service = Service(executable_path=CHROME_DRIVER)
browser = webdriver.Chrome(
    service=chrome_service,
    options=chrome_options
)

chrome_options.add_argument('--headless')

query = 'teste'
browser.get(f'https://twitter.com/search?q={query}&src=typed_query')
for i in range(20):
    sleep(1)
    browser.execute_script("window.scrollBy(0,500000)","")
sleep(WAIT_TIME)
timeline = WebDriverWait(browser, WAIT_TIME).until(
    EC.presence_of_element_located(
      (By.XPATH , '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div')
    )
)
posts = timeline.find_elements(By.CSS_SELECTOR, '[data-testid="tweetText"]')
content = [el.text for el in posts 
         if el.text != '']

[print(f'\n{i}: {text}') for i, text in enumerate(content)]

browser.execute_script("window.scrollBy(0,90000000000000000000000000000000000)","") 
sleep(4)