import os

from selene import command, have, browser


def test_student_registration_form(browser_set):
    # WHEN
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('testcase@gmail.com')
    browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()  # this is Xpath
    '''
    browser_set.all('[name=gender]').element_by(have.value('Female')).element('./folowing-sibling::*').click()
    browser_set.element('[name=gender][value=Female]+label').click()
    browser_set.all('.custom-radio').element_by(have.texts('Female')).click()
    '''

    browser.element('#userNumber').type("1234567891")

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="11"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value=1991]').click()
    browser.element('[aria-label="Choose Monday, December 9th, 1991"]').click()

    browser.element('#subjectsInput').type('Commerce').press_enter()
    browser.element('[for=hobbies-checkbox-1]').perform(command.js.scroll_into_view)
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('#currentAddress').type("Republic of Belarus")

    browser.element('#uploadPicture').send_keys(os.path.abspath('./foto.jpg'))

    select_option(selector='#state', text='Haryana')
    select_option(selector='#city', text='Merrut')

    browser.element('#submit').click()

    # THEN
    browser.element('.table').all('td:nth-of-type(2)').should(have.texts(
        'Ivan',
        'Ivanov',
        'testcase@gmail.com',
        'Female'
        '1234567891',
        'HellloHello',
        'Republic of Belarus'
    ))


def select_option(selector, text):
    browser.element(selector).click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(text)).click()
    browser.element('#city').click()
