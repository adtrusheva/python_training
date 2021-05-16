# -*- coding: utf-8 -*-
from model.contact import Contact
import allure


def test_add_contact(app, json_contacts, db, check_ui):
    contact = json_contacts
    old_contacts = given_contact_list(db)
    create_contact(app, contact)
    new_contacts = given_contact_list(db)
    check_contacts(app, old_contacts, new_contacts, contact, check_ui)


@allure.step('Given a contact list')
def given_contact_list(db):
    return db.get_contact_list()


@allure.step('When I add the contact "{contact}" to the list')
def create_contact(app, contact):
    app.contact.create(contact)


@allure.step('Then the new contact list is equal to the old list with the added contact')
def check_contacts(app, old_contacts, new_contacts, contact, check_ui):
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
