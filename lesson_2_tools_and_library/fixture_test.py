import pytest


@pytest.fixture()
def open_browser():
    b = "browser"
    yield "browser"


@pytest.fixture()
def create_user(open_browser):
    return 35


@pytest.fixture()
def test_body(open_browser):
    pass
    # Перейти на страницу логина
    # Вывести логин и пароль
    # Нажать ОК
    # Убедится что мы перешли на страницу профиля
