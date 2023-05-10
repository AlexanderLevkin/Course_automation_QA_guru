from typing import Literal, Callable

import pytest
from selene.support.shared import browser
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
def browser_set(url):
    browser.config.driver = webdriver.Chrome(ChromeDriverManager().install())
    browser.driver.set_window_size(1024, 720)
    browser.open(url)
    yield browser
    browser.quit()
