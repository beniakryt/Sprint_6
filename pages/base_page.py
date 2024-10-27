from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    def click_to_element(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.find_element(*locator).click()

    def add_text_to_element(self, locator, text, timeout=10):
        element = self.find_element_with_wait(locator, timeout)
        element.clear()  # Очистка поля перед вводом
        element.send_keys(text)

    def get_text_from_element(self, locator, timeout=10):
        return self.find_element_with_wait(locator, timeout).text

    def scroll_to_element(self, locator, timeout=10):
        element = self.find_element_with_wait(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator
