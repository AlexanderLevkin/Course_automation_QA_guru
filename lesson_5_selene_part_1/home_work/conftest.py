from typing import Literal, Callable

import pytest
from selene.support.shared import browser as selene_browser
from selene import Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def url():
    return 'https://demoqa.com/automation-practice-form'


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
