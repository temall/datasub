import pytest
from playwright.sync_api import Page

from pages.quote_page import Quote


@pytest.fixture
def quote(page: Page):
    return Quote(page)
