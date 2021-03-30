# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact_firstname(app):
    app.contact.edit_first_contact(Contact(firstname='Petr'))


def test_edit_contact_middlename(app):
    app.contact.edit_first_contact(Contact(middlename='Vasilevich'))


def test_edit_contact_lastname(app):
    app.contact.edit_first_contact(Contact(lastname='Durov'))