import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):

    @allure.step('Проверяем и закрываем окно cookie')
    def accept_cookie_consent(self):
        try:
            self.click_to_element(OrderPageLocators.COOKIE_CONSENT_BUTTON)
        except:
            pass

    @allure.step('Нажимаем на кнопку "Заказать"')
    def click_order_button(self, button_locator):
        self.accept_cookie_consent()
        self.click_to_element(button_locator)

    @allure.step('Заполняем форму заказа')
    def fill_order_form(self, name, last_name, address, phone, date):
        self.click_to_element(OrderPageLocators.NAME_FIELD)
        self.add_text_to_element(OrderPageLocators.NAME_FIELD, name)

        self.click_to_element(OrderPageLocators.LAST_NAME_FIELD)
        self.add_text_to_element(OrderPageLocators.LAST_NAME_FIELD, last_name)

        self.click_to_element(OrderPageLocators.ADDRESS_FIELD)
        self.add_text_to_element(OrderPageLocators.ADDRESS_FIELD, address)

        self.click_to_element(OrderPageLocators.STATION_DROPDOWN)
        self.click_to_element(OrderPageLocators.STATION_ADDRESS)

        self.click_to_element(OrderPageLocators.PHONE_FIELD)
        self.add_text_to_element(OrderPageLocators.PHONE_FIELD, phone)
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

        self.click_to_element(OrderPageLocators.DATE_FIELD)
        date_field = self.find_element_with_wait(OrderPageLocators.DATE_FIELD)
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)

        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_OPTION)

        self.click_to_element(OrderPageLocators.COLOR_CHECKBOX)

        self.click_to_element(OrderPageLocators.ORDER_CONFIRM_BUTTON)
        self.click_to_element(OrderPageLocators.CONFIRM_POPUP_BUTTON)

    @allure.step('Проверяем успешное оформление заказа')
    def check_order_success(self):
        return self.get_text_from_element(OrderPageLocators.SUCCESS_MESSAGE)

