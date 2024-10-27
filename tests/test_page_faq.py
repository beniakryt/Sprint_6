import allure
import pytest
from data import BASE_URL, ANSWER_1, ANSWER_2, ANSWER_3, ANSWER_4, ANSWER_5, ANSWER_6, ANSWER_7, ANSWER_8
from pages.main_page import MainPage


class TestMainPage:

    @allure.description('Проверяем, что при клике на вопрос ответ правильный')
    @pytest.mark.parametrize(
        'num, result',
        [
            (0, ANSWER_1),
            (1, ANSWER_2),
            (2, ANSWER_3),
            (3, ANSWER_4),
            (4, ANSWER_5),
            (5, ANSWER_6),
            (6, ANSWER_7),
            (7, ANSWER_8)
        ]
    )
    def test_questions_and_answers(self, driver, num, result):
        driver.get(BASE_URL)
        main_page = MainPage(driver)
        actual_answer = main_page.get_answer_text(num)
        assert actual_answer == result, f"Ожидаем '{result}' получили '{actual_answer}'"
