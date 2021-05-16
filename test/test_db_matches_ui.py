from model.contact import Contact
import re
import allure


def test_contact_list(app, db):
    ui_list = given_contacts_from_ui(app)
    db_list = given_contacts_from_db(app, db)
    equals_contacts(ui_list, db_list)


@allure.step('Given a contacts from ui')
def given_contacts_from_ui(app):
    return app.contact.get_contact_list()


@allure.step('Given a contacts from database')
def given_contacts_from_db(app, db):

    def clean(contact):
        return Contact(
            id=contact.id,
            firstname=contact.firstname.strip(),
            lastname=contact.lastname.strip(),
            address=contact.address.strip(),
            all_phones_from_home_page=merge_phones_like_on_home_page(contact),
            all_emails_from_home_page=merge_emails_like_on_home_page(contact),
        )

    return map(clean, db.get_contact_list())


@allure.step('Then the contact list from ui equal contact list from db')
def equals_contacts(ui_list, db_list):
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)



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
