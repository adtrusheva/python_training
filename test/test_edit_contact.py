# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact_firstname(app):
    if app.contact.count() == 0:
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
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(firstname='Petr'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(middlename='Vasilevich'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(lastname='Durov'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)