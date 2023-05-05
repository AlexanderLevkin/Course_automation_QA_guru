import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_manager():
    browser.config.timeout = 3.0
    print("ENTER")

    yield
    print("EXIT")
    browser.quit()
