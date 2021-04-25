# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_contact_firstname(app, db, check_ui):
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
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname='Petr')
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[index].lastname
    app.contact.edit_contact_by_id(contact, contact.id)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_edit_contact_middlename(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    app.contact.edit_first_contact(Contact(middlename='Vasilevich'))
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_edit_contact_lastname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(lastname='Durov'))
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
