import pytest
import selene

@pytest.fixture(scope= 'function', autouse = True)
def test_browser_managment():
    selene.browser.config.hold_browser_open = True
    selene.browser.config.browser_name = 'firefox'
    selene.browser.config.window_width = 700
    selene.browser.config.window_height = 7000
    selene.browser.config.base_url = ('https://demoqa.com/automation-practice-form')
    yield