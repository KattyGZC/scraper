from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
import time
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
def start_scraping(content_type, category, format, report_name):
    try:
        url = 'https://www.datosabiertos.gob.pe/'
        options = webdriver.ChromeOptions()
        prefs = {"download.default_directory": f"{BASE_DIR}"}
        options.add_experimental_option("prefs", prefs)
        options.add_argument('--start-maximized')
        options.add_argument('-–disable-extensions')
        driver_path = f'{BASE_DIR}\\chromedriver.exe'
        driver_web = webdriver.Chrome(
            executable_path=driver_path,
            chrome_options=options)
        driver_web.get(url)
        search_data(driver_web, content_type, category, format, report_name)
        get_data(driver_web, report_name)
        return True

    except Exception as error:
        return f'Ha ocurrido un error: {error}'


def search_data(driver_web, content_type, category, format, report_name):
    try:
        content_type = driver_web.find_element(
            By.PARTIAL_LINK_TEXT, content_type)
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
        search_button = driver_web.find_element(
            By.ID, 'edit-submit-dkan-datasets')
        search_button.click()
        time.sleep(3)
        link_data = driver_web.find_element(
            By.PARTIAL_LINK_TEXT, report_name.capitalize())
        link_data.click()
        time.sleep(5)
        return True
    except Exception as e:
        return e


def get_data(driver_web,):

    try:
        file = driver_web.find_elements(
            By.CLASS_NAME, 'btn btn-primary data-link'.replace(' ', '.'))
        file[2].click()
        time.sleep(10)
        return True
    except Exception as e:
        return e


def process_data(filename):
    data = read_data(filename)
    data_classification(data)
    return True


def read_data(file):
    import chardet
    import zipfile
    try:
        path_zip = f"{BASE_DIR}\\{file}"
        path_extraction = f"{BASE_DIR}"
        password = None
        file_zip = zipfile.ZipFile(path_zip, "r")
        try:
            file_zip.extractall(pwd=password, path=path_extraction)
        except BaseException:
            pass
        file_zip.close()
    except Exception as e:
        raise e
    with open(file_zip.namelist()[0], 'rb') as rawdata:
        result = chardet.detect(rawdata.read(100000))
    df = pd.read_csv(file, encoding=result['encoding'], sep=',')
    return df


def data_classification(data):
    try:
        columns = data.columns.tolist()
        regions = data[columns[1]].unique()
        for region in regions:
            filter = data[columns[1]] == region
            (data[filter]).to_csv(
                f'{BASE_DIR}\\scraper_pe\\classified_files\\{region.lower()}.csv')
        return True
    except Exception as e:
        return e
