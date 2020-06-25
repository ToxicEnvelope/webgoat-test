from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class BasePage:
    def __init__(self, wd):
        self._wd = wd
    
    def click(self, locator):
        WebDriverWait(self._wd, 15, 250) \
            .until(EC.visibility_of_element_located(locator)).click()

    def send_keys(self, locator, word):
        elem = WebDriverWait(self._wd, 15, 250) \
            .until(EC.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(word)



if __name__ == "__main__":

    EMAIL_INPUT = (By.CSS_SELECTOR, "#exampleInputEmail1")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#exampleInputPassword1")
    SUBMIT_BTN = (By.CSS_SELECTOR, "#main-content > form > button")


    PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    CHROME_BIN = os.path.join(os.path.join(PATH, "bin"), "chromedriver")
    
    driver = webdriver.Chrome(CHROME_BIN)
    driver.get("http://localhost:8080/WebGoat/login")
    page = BasePage(driver)
    page.send_keys(EMAIL_INPUT, "seeker")
    page.send_keys(PASSWORD_INPUT, "seeker")
    page.click(SUBMIT_BTN)
    driver.quit()