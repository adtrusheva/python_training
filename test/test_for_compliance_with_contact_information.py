import re
import allure


def test_contact_data_on_home_page(app):
    contact_from_home_page = given_first_contact_from_home_page(app)
    contact_from_edit_page = given_first_contact_from_edit_page(app)
    equals_phones(contact_from_home_page, contact_from_edit_page)
    equals_emails(contact_from_home_page, contact_from_edit_page)
    equals_firstname(contact_from_home_page, contact_from_edit_page)
    equals_lastname(contact_from_home_page, contact_from_edit_page)
    equals_address(contact_from_home_page, contact_from_edit_page)


@allure.step('Given a first contact from home page')
def given_first_contact_from_home_page(app):
    return app.contact.get_contact_list()[0]


@allure.step('Given a first contact from edit page')
def given_first_contact_from_edit_page(app):
    return app.contact.get_contact_info_from_edit_page(0)


@allure.step('Then the phones from home page equals phones from edit page')
def equals_phones(contact_from_home_page, contact_from_edit_page):
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


@allure.step('Then the emails from home page equals emails from edit page')
def equals_emails(contact_from_home_page, contact_from_edit_page):
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


@allure.step('Then the firstname from home page equals firstname from edit page')
def equals_firstname(contact_from_home_page, contact_from_edit_page):
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname


@allure.step('Then the lastname from home page equals lastname from edit page')
def equals_lastname(contact_from_home_page, contact_from_edit_page):
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname


@allure.step('Then the address from home page equals address from edit page')
def equals_address(contact_from_home_page, contact_from_edit_page):
    assert contact_from_home_page.address == contact_from_edit_page.address



def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                (filter(lambda x: x is not None,
                                        [contact.home, contact.mobile, contact.work, contact.phone2])))))


def clear(s):
    return re.sub("[() -]", "", s)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            (filter(lambda x: x is not None,
                                    [contact.email, contact.email2, contact.email3]))))
