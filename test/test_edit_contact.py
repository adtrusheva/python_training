# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange
import allure


def test_edit_contact(app, db, check_ui):
    old_contacts = given_non_empty_contact_list(app, db)
    index = random_contact_index(old_contacts)
    contact = given_updated_contact_by_index(old_contacts, index)
    edit_contact(app, contact)
    assert len(old_contacts) == app.contact.count()
    check_contacts(app, db, old_contacts, contact, index, check_ui)


@allure.step('Given a non-empty contact list')
def given_non_empty_contact_list(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(photo='contact_photo.jpg',
                                   firstname='Igor',
                                   middlename='Victirivich',
                                   lastname='Pushkin',
                                   nickname='geek',
                                   title='pure',
                                   company='OutStaf',
                                   address='Moscow, Red Proletarskiy',
                                   home='92',
                                   mobile='983726000',
                                   work='9284730000',
                                   fax='8473700000',
                                   email='qwertys1@mail.ru',
                                   email2='qwertys2mail.ru',
                                   email3='qwertys3@mail.ru',
                                   homepage='wasd.com',
                                   bday='25',
                                   bmonth='June',
                                   byear='1995',
                                   aday='9',
                                   amonth='May',
                                   ayear='1999',
                                   address2='Moscow, Serbryanicheskaya Naberezhnaya',
                                   phone2='928473001',
                                   notes='python'))
    return db.get_contact_list()


@allure.step('Given a random index contact from the list')
def random_contact_index(old_contacts):
    index = randrange(len(old_contacts))
    return index


@allure.step('Given a contact by index to the list')
def given_updated_contact_by_index(old_contacts, index):
    contact = Contact(firstname='Petr', lastname='Petrov', middlename='Petrovich')
    contact.id = old_contacts[index].id
    return contact


@allure.step('Given a contact list')
def given_contact_list(db):
    return db.get_contact_list()


@allure.step('When I edit the contact "{contact}" from the list')
def edit_contact(app, contact):
    app.contact.edit_contact_by_id(contact, contact.id)


@allure.step('Then the new contact list is equal to the old list with the edited contact')
def check_contacts(app, db, old_contacts, contact, index, check_ui):
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
