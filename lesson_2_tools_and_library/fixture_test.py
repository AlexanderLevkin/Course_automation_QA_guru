from selene import have, be


def test_google_search_positive(browser):
    search = 'selene python'
    expected_result = 'yashaka/selene: User-oriented Web UI browser tests in Python'

    browser.element('[name="q"]').should(be.blank).type(search).press_enter()
    browser.element('[id="search"]').should(have.text(expected_result))


def test_google_search_negative(browser):
    search = 'iabsiujfokjaospfjaigfnioasjgoksamngoiasmg'
    expected_result = 'Результатов: примерно 0'

    browser.element('[name="q"]').should(be.blank).type(search).press_enter()
    browser.element('div#result-stats').should(have.text(expected_result))
