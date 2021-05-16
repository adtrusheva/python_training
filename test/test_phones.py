import re
import allure


def test_phones_on_view_page(app):
    contact_from_view_page = given_first_contact_from_view_page(app)
    contact_from_edit_page = given_first_contact_from_edit_page(app)
    equals_home_phone(contact_from_view_page, contact_from_edit_page)
    equals_mobile_phone(contact_from_view_page, contact_from_edit_page)
    equals_work_phone(contact_from_view_page, contact_from_edit_page)
    equals_home_phone2(contact_from_view_page, contact_from_edit_page)


@allure.step('Given a first contact from home page')
def given_first_contact_from_view_page(app):
    return app.contact.get_contact_from_view_page(0)


@allure.step('Given a first contact from edit page')
def given_first_contact_from_edit_page(app):
    return app.contact.get_contact_info_from_edit_page(0)


@allure.step('Then the home phone from view page equals home phone from edit page')
def equals_home_phone(contact_from_view_page, contact_from_edit_page):
    assert contact_from_view_page.home == contact_from_edit_page.home


@allure.step('Then the mobile phone from view page equals mobile phone from edit page')
def equals_mobile_phone(contact_from_view_page, contact_from_edit_page):
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile


@allure.step('Then the work phone from view page equals work phone from edit page')
def equals_work_phone(contact_from_view_page, contact_from_edit_page):
    assert contact_from_view_page.work == contact_from_edit_page.work


@allure.step('Then the home phone2 from view page equals home phone2 from edit page')
def equals_home_phone2(contact_from_view_page, contact_from_edit_page):
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                                (filter(lambda x: x is not None,
                                        [contact.home, contact.mobile, contact.work, contact.phone2])))))
