import pytest
from selene.support.shared import browser
from selene import be, have


def test_finds_selene():
    browser.config.hold_browser_open = True
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

    results = browser.all('#rso>div')
    results.should(have.size_greater_than_or_equal(6))


def test_finds_selene_with_refined_query():
    browser.config.hold_browser_open = True
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
    results = browser.all('#rso>div')
    results.should(have.size_greater_than_or_equal(6))

    browser.element('[name="q"]').type(' yashaka github ').press_enter()
    results.first.element('h3').click()
    browser.should(have.tag_containing('yashaka/selene'))


browser.quit()
