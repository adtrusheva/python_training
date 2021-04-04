# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(
        photo='contact_photo.jpg',
        firstname='Fedor',
        middlename='Ivanovich',
        lastname='Truhin',
        nickname='pups',
        title='funny',
        company='Self',
        address='Moscow, Color Bulvar',
        home='34',
        mobile='983726475',
        work='9284737264',
        fax='8473748394',
        email='4662e@mail.ru',
        email2='63g73mail.ru',
        email3='fgr63hf@mail.ru',
        homepage='terwye.com',
        bday='11',
        bmonth='May',
        byear='1991',
        aday='5',
        amonth='June',
        ayear='1995',
        address2='Moscow, Red Bulvar',
        phone2='928473627',
        notes='port'
    )
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='', lastname='')
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)