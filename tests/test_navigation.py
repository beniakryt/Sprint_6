import allure
from data import BASE_URL
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
import time


class TestNavigation:
    @allure.description('Проверка перехода на главную страницу по логотипу «Самоката»')
    def test_scooter_logo_navigation(self, driver):
        driver.get(BASE_URL)
        main_page = MainPage(driver)

        main_page.click_order_button(MainPageLocators.TOP_ORDER_BUTTON)
        main_page.click_scooter_logo()

        assert driver.current_url == BASE_URL, "Не удалось вернуться на главную страницу"

    @allure.description('Проверка перехода на главную страницу Дзена по логотипу Яндекса')
    def test_yandex_logo_navigation(self, driver):
        driver.get(BASE_URL)
        main_page = MainPage(driver)

        main_page.click_order_button(MainPageLocators.TOP_ORDER_BUTTON)
        main_page.click_yandex_logo()

        driver.switch_to.window(driver.window_handles[1])

        time.sleep(3)

        assert "dzen.ru" in driver.current_url, "Не удалось открыть главную страницу Дзена"

