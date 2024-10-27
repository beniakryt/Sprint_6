from selenium.webdriver.common.by import By

class OrderPageLocators:

    TOP_ORDER_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Button__ra12g") and text()="Заказать"]')
    BOTTOM_ORDER_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Button__ra12g Button_Middle__1CSJM") and text()="Заказать"]')
    NAME_FIELD = (By.XPATH, '//input[contains(@class, "Input_Input__1iN_Z Input_Responsible__1jDKN") and @placeholder="* Имя"]')
    LAST_NAME_FIELD = (By.XPATH, '//input[contains(@class, "Input_Input__1iN_Z Input_Responsible__1jDKN") and @placeholder="* Фамилия"]')
    ADDRESS_FIELD = (By.XPATH, '//input[contains(@class, "Input_Input__1iN_Z Input_Responsible__1jDKN") and @placeholder="* Адрес: куда привезти заказ"]')
    STATION_DROPDOWN = (By.XPATH, '//input[contains(@class, "select-search__input") and @placeholder="* Станция метро"]')
    STATION_ADDRESS = (By.XPATH, '//li[@data-value="1"]')
    PHONE_FIELD = (By.XPATH, '//input[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and @placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Далее"]')
    DATE_FIELD = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, '//div[@class="Dropdown-placeholder" and text()="* Срок аренды"]')
    RENTAL_PERIOD_OPTION = (By.XPATH, '//div[@class="Dropdown-option" and text()="сутки"]')
    COLOR_CHECKBOX = (By.ID, 'black')
    COMMENT_DELIVERY = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    ORDER_CONFIRM_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and contains(text(), "Заказать")]')
    CONFIRM_POPUP_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Да"]')
    SUCCESS_MESSAGE = (By.XPATH, '//div[contains(text(), "Заказ оформлен")]')
    COOKIE_CONSENT_BUTTON = (By.XPATH, '//button[@class = "App_CookieButton__3cvqF" and text ()="да все привыкли"]')

