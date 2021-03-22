# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(
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
    ))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(
        photo='',
        firstname='',
        middlename='',
        lastname='',
        nickname='',
        title='',
        company='',
        address='',
        home='',
        mobile='',
        work='',
        fax='',
        email='',
        email2='',
        email3='',
        homepage='',
        bday='',
        bmonth='',
        byear='',
        aday='',
        amonth='',
        ayear='',
        address2='',
        phone2='',
        notes=''
    ))
    app.session.logout()
