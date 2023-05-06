from selene import command, have, browser


def test_filed_form(browser_set):
    browser_set.element('#firstName').type("Alexander")
    browser_set.element('#lastName').type("QA")
    browser_set.element('#userEmail').type("testcase@gmail.com")
    browser_set.element('[for="gender-radio-1"]').click()
    browser_set.element('#userNumber').type("1234567891")
    browser_set.element('#dateOfBirthInput').click()
    browser_set.element('.react-datepicker__month-select').click()
    browser_set.element('[value="11"]').click()
    browser_set.element('.react-datepicker__year-select').click()
    browser_set.element('[value="1991"]').click()
    browser_set.element('[aria-label="Choose Monday, December 9th, 1991"]').click()
    browser_set.element('#subjectsInput').type('HellloHello').press_enter()
    browser_set.element('[for="hobbies-checkbox-1"]').click()
    browser_set.element('#currentAddress').type("Republic of Belarus")
    browser_set.element('#state').click()
    browser_set.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser_set.element('#react-select-4-input').type('Merrut').press_enter()
    browser_set.element('#submit').click()
    browser_set.all('.table-responsive td:nth-child(2)').should(have.texts(
        'Alexander',
        'QA',
        'testcase@gmail.com',
        '+375444444444',
        'HellloHello',
        'Republic of Belarus'
    ))


