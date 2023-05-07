import os

from selene import command, have, browser


def test_student_registration_form(browser_set):
    # WHEN
    browser_set.element('#firstName').type('Ivan')
    browser_set.element('#lastName').type('Ivanov')
    browser_set.element('#userEmail').type('testcase@gmail.com')
    browser_set.all('[name=gender]').element_by(have.value('Male')).element('..').click()  # this is Xpath
    '''
    browser_set.all('[name=gender]').element_by(have.value('Female')).element('./folowing-sibling::*').click()
    browser_set.element('[name=gender][value=Female]+label').click()
    browser_set.all('.custom-radio').element_by(have.texts('Female')).click()
    '''

    browser_set.element('#userNumber').type("1234567891")

    browser_set.element('#dateOfBirthInput').click()
    browser_set.element('.react-datepicker__month-select').click()
    browser_set.element('[value="11"]').click()
    browser_set.element('.react-datepicker__year-select').click()
    browser_set.element('[value="1991"]').click()
    browser_set.element('[aria-label="Choose Monday, December 9th, 1991"]').click()

    browser_set.element('#subjectsInput').type('Commerce').press_enter()
    browser_set.element('[for=hobbies-checkbox-1]').perform(command.js.scroll_into_view)
    browser_set.element('[for=hobbies-checkbox-1]').click()
    browser_set.element('#currentAddress').type("Republic of Belarus")

    browser_set.element('#uploadPicture').send_keys(os.path.abspath('./foto.jpg'))

    browser_set.element('#state').click()
    browser_set.all('[id^=react-select][id*=option]').element_by(have.exact_text('Haryana')).click()
    browser_set.element('#city').click()
    browser_set.all('[id^=react-select][id*=option]').element_by(have.exact_text('Merrut')).click()

    browser_set.element('#submit').click()

    # THEN
    browser_set.element('.table').all('td:nth-of-type(2)').should(have.texts(
        'Ivan',
        'Ivanov',
        'testcase@gmail.com',
        'Female'
        '1234567891',
        'HellloHello',
        'Republic of Belarus'
    ))


