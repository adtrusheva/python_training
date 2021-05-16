# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import allure


def test_delete_some_contact(app, db, check_ui):
    old_contacts = given_non_empty_contact_list(app, db)
    contact = random_contact(old_contacts)
    delete_contact(app, contact)
    new_contacts = given_contact_list(db)
    assert len(old_contacts) - 1 == len(new_contacts)
    check_contacts(app, old_contacts, new_contacts, contact, check_ui)


@allure.step('Given a non-empty contact list')
def given_non_empty_contact_list(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    return db.get_contact_list()


@allure.step('Given a random contact to the list')
def random_contact(contacts):
    return random.choice(contacts)


@allure.step('Given a contact list')
def given_contact_list(db):
    return db.get_contact_list()


@allure.step('When I delete the contact "{contact}" from the list')
def delete_contact(app, contact):
    app.contact.delete_contact_by_id(contact.id)


@allure.step('Then the new contact list is equal to the old list with the deleted contact')
def check_contacts(app, old_contacts, new_contacts, contact, check_ui):
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_group_list(),
                                                                     key=Contact.id_or_max)
