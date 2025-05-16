import pytest
import allure
from playwright.sync_api import Page

from pages.quote_page import Quote, free_quote

title_1 = "Проверка отправки запроса при корректно заполненной форме"


@allure.title(title_1)
@allure.testcase("https://url/1", title_1)
def test_quote_form_positive(page: Page,
                             quote: Quote):
    page.goto("https://qatest.datasub.com/")
    page.locator(free_quote).first.click()
    print(page.locator("#quoteStatus").text_content())
    quote.fill_quote_form(name="test", email="example@mail.ru", service="Service 3", message="test message")
    quote.submit_quote()
    quote.check_quote_status(message="Форма отправлена")


title_2 = "Проверка отправки запроса при некорректно заполненной форме"


@allure.title(title_2)
@allure.testcase("https://url/2", title_2)
def test_quote_form_negative(page: Page,
                             quote: Quote):
    page.goto("https://qatest.datasub.com/")
    page.locator(free_quote).first.click()
    quote.fill_quote_form(name="test", email="example@почта.ru", service="Service 2", message="test")
    quote.submit_quote()
    assert "Форма отправлена" not in page.locator("#quoteStatus").text_content()
