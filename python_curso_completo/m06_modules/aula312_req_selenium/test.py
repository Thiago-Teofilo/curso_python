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

browser.get(f'https://www.linkedin.com/search/results/people/?connectionOf=%5B%22ACoAABsgSVcBbAGk8aqbaeQk95EZmJd6uUdr6EU%22%5D&network=%5B%22S%22%5D&origin=FACETED_SEARCH&sid=Q~f')

input("Pressione [Enter] após fazer login")

conn_list = browser.find_elements(By.CLASS_NAME, 'artdeco-button--2')
browser.execute_script("arguments[0].click();", conn_list[0])
sleep(3)