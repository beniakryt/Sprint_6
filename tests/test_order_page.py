import allure
import pytest
from data import BASE_URL
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators


class TestOrderPage:

    @allure.description('Тестируем заказ самоката с двумя разными наборами данных')
    @pytest.mark.parametrize(
        "button_locator, name, last_name, address, phone, date",
        [
            (OrderPageLocators.TOP_ORDER_BUTTON, "Иван", "Иванов", "ул. Пушкина, д. 1", "89999999999",
             "31.12.2024"),
            (OrderPageLocators.BOTTOM_ORDER_BUTTON, "Анна", "Смирнова", "ул. Ленина, д. 15",
             "89998887766", "01.01.2024")
        ]
    )
    def test_order_scooter(self, driver, button_locator, name, last_name, address, phone, date):
        driver.get(BASE_URL)
        order_page = OrderPage(driver)

        order_page.click_order_button(button_locator)

        order_page.fill_order_form(name, last_name, address, phone, date)

        success_message = order_page.get_order_success()
        assert "Заказ оформлен" in success_message, "Ожидалось сообщение об успешном заказе"

