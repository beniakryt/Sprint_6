from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTION_LOCATOR = By.XPATH, '//*[@id="accordion__heading-{}"]'
    ANSWER_LOCATOR = By.XPATH, '//*[@id="accordion__panel-{}"]/p'
    QUESTION_LOCATOR_8 = By.XPATH, '//*[@id="accordion__heading-7"]'
    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    TOP_ORDER_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Button__ra12g") and text()="Заказать"]')
