from selenium import webdriver
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv
import time
import os

if __name__ == "__main__":
    chrome_driver_binary = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(chrome_driver_binary)
    driver.get('https://tts.sutd.edu.sg/')

    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    load_dotenv(os.path.join(BASEDIR, '.env'))

    PASSWORD = os.getenv('PASSWORD')
    ID = os.getenv('ID')

    A = True
    try:
        driver.find_elements_by_id('pgContent1_uiLoginid')[0].send_keys(ID)
        driver.find_elements_by_id('pgContent1_uiPassword')[0].send_keys(PASSWORD)
        time.sleep(10)


        #Daily Declaration
        driver.get('https://tts.sutd.edu.sg/tt_daily_dec_user.aspx')
        driver.find_elements_by_id('pgContent1_cbSetToNo')[0].click()
        driver.find_elements_by_id('pgContent1_btnSave')[0].click()
        driver.switch_to.alert.accept()

        for x in range(2):
            driver.get('https://tts.sutd.edu.sg/tt_temperature_taking_user.aspx')
            select = Select(driver.find_element_by_id('pgContent1_uiTemperature'))
            select.select_by_visible_text('Less than or equal to 37.6°C')
            driver.find_elements_by_id('pgContent1_btnSave')[0].click()
            driver.switch_to.alert.accept()
        print("successfully recorded")
        driver.close()
    except (IndexError):
        print("Fail, need to try again!")
        driver.close()
