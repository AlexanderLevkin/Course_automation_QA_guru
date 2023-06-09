from ..demoqa_tests.data import users
from ..demoqa_tests.model import controls, pages
from ..demoqa_tests.model.pages import practice_form


def test_student_fail_to_register_without_required_fields_filled():
    practice_form.given_opened()

    ...


def test_student__registers_after_fixing_validation_errors_of_required_fields_not_filled():
    practice_form.given_opened()

    # fill some fields

    # browser.element('#submit').click()
    admin = users.admin

    practice_form.submit_data('Olga', 'YA', 'mail@example.com')
    practice_form.submit_data(admin)

    pages.practice_form.select_hobbies('Sports', 'Music')

    controls.checkboxes.select(practice_form.hobbies, by_texts=('Sports', 'Music'))

    # practice_form.submit()

    # practice_form.submit.click()

    # asssert validation errors
    practice_form.should_have_validations_of_number(4)
    practice_form.should_have_validation_errors()

    # fill all required fields

    # browser.element('#submit').click()

    submit.click()

