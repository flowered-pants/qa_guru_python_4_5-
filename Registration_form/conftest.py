import pytest
import selene
from selene import browser
from selene import have, be


@pytest.fixture(scope='function', autouse=True)
def browser_managment():
    browser.config.hold_browser_open = True
    browser.config.type_by_js = True
    browser.config.browser_name = 'firefox'
    browser.config.window_width = 700
    browser.config.window_height = 7000
    browser.config.base_url = ('https://demoqa.com')
    yield
