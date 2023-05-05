import pytest
from selene.support.shared import browser as selene_browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def url():
    return "https://www.google.com/"


@pytest.fixture()
def set_driver():
    selene_browser.config.driver = webdriver.Chrome(ChromeDriverManager().install())
    return selene_browser.config.driver


@pytest.fixture()
def maximized_window():
    selene_browser.driver.set_window_size(1024, 720)


@pytest.fixture()
def browser(url, set_driver, maximized_window):
    selene_browser.open(url)
    yield selene_browser
    selene_browser.quit()
