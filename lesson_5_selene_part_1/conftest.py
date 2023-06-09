from typing import Literal, Callable

import pytest
from selene.support.shared import browser as selene_browser
from selene import Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    selene_browser.config.timeout = 3.0
    # commented after we started to cover more than one web app in tests
    # browser.config.base_url = 'https://www.google.com'

    yield

    selene_browser.quit()


SupportedBrowsers = Literal['chrome', 'firefox']


@pytest.fixture(scope='function')
def with_new_browser():
    future_browsers = []

    def new_browser(name: SupportedBrowsers = 'chrome'):
        nonlocal future_browsers
        if name == 'chrome':
            future_browser = Browser(
                Config(driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))))
        elif name == 'firefox':
            future_browser = Browser(
                Config(driver=webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))))
        else:
            raise Exception(f'Browser «{name}» is not supported! please, use «chrome» or «firefox» values')

        future_browsers.append(future_browser)

        return future_browser

    yield new_browser

    for future_browser in future_browsers:
        future_browser.quit()


@pytest.fixture()
def set_driver():
    selene_browser.config.driver = webdriver.Chrome(ChromeDriverManager().install())
    return selene_browser.config.driver


@pytest.fixture()
def maximized_window():
    selene_browser.driver.set_window_size(1024, 720)


@pytest.fixture()
def browser_set(url, set_driver, maximized_window):
    selene_browser.open(url)
    yield selene_browser
    selene_browser.quit()
