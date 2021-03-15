from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys

def getChromeDriver():
    chrome_options = Options()
    if sys.argv[1] == '--headless':
        chrome_options.add_argument("--headless")
        print('\n Ejecutando Chrome en modo Headless \n')
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="drivers/chromedriver")
    return driver
