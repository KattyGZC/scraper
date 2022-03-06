from traceback import format_list
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Scraper.settings import BASE_DIR
import time
import pandas as pd


def start_scraping(content_type, category, format, report_name):
    try:
        url = 'https://www.datosabiertos.gob.pe/'
        options = webdriver.ChromeOptions()
        prefs={"download.default_directory":f"{BASE_DIR}"}
        options.add_experimental_option("prefs", prefs)
        options.add_argument('--start-maximized')
        options.add_argument('-–disable-extensions')
        driver_path = f'{BASE_DIR}\chromedriver.exe'
        driver_web = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
        driver_web.get(url)
        search_data(driver_web, content_type, category, format, report_name)
        get_data(driver_web)

    except Exception as error:
        return f'Ha ocurrido un error: {error}'

def search_data(driver_web, content_type, category, format, report_name):
    content_type=driver_web.find_element(By.PARTIAL_LINK_TEXT, content_type)
    content_type.click()
    time.sleep(3)
    category = driver_web.find_element(By.PARTIAL_LINK_TEXT, category)
    category.click()
    time.sleep(3)
    h2_elements = driver_web.find_elements(By.TAG_NAME, 'h2')
    for element in h2_elements:
        if element.text == 'Formato':
            format_list = element
            format_list.click()
            time.sleep(3)
            break
    format_option = driver_web.find_element(By.PARTIAL_LINK_TEXT, format)
    format_option.click()
    time.sleep(3)
    search_file = driver_web.find_element(By.ID, 'edit-query')
    search_file.send_keys(report_name)
    search_button = driver_web.find_element(By.ID, 'edit-submit-dkan-datasets')
    search_button.click()
    time.sleep(3)
    link_data = driver_web.find_element(By.PARTIAL_LINK_TEXT, report_name.capitalize())
    link_data.click()
    time.sleep(5)

    return True

def get_data(driver_web):
    file = driver_web.find_element(By.CLASS_NAME, 'btn btn-primary data-link'.replace(' ','.'))
    file.click()
    time.sleep(10)
    return True