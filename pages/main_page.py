import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Кликаем на вопрос и получаем ответ')
    def get_answer_text(self, num):
        question_locator = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        answer_locator = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)

        self.scroll_to_element(question_locator)
        self.click_to_element(question_locator)

        return self.get_text_from_element(answer_locator)

    @allure.step('Нажимаем на кнопку "Заказать"')
    def click_order_button(self, button_locator):
        self.click_to_element(button_locator)

    @allure.step('Кликаем на логотип "Самоката"')
    def click_scooter_logo(self):
        self.click_to_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Кликаем на логотип Яндекса')
    def click_yandex_logo(self):
        self.click_to_element(MainPageLocators.YANDEX_LOGO)





