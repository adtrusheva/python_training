# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_address(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(maxlen):
    numeral = string.digits
    return [random.choice(numeral) for i in range(random.randrange(maxlen))]


def random_email(prefix, maxlen):
    mail = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(mail) for i in range(random.randrange(maxlen))]) + '@mail.example'


def random_website(prefix, maxlen):
    site = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(site) for i in range(random.randrange(maxlen))]) + '.com'


def random_month():
    month_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    return random.choice(month_list)


def random_year():
    return str(random.randint(1900, 2020))


def random_day():
    return str(random.randint(1, 31))


def random_photo():
    photo_list = [
        "contact_photo.jpg",
        "contact_photo_edit.png",
    ]

    return random.choice(photo_list)


testdata = [Contact(firstname="", lastname="", middlename="")] \
           + \
           [
               Contact(firstname=random_string("firstname", 8), lastname=random_string("lastname", 8),
                       middlename=random_string("middlename", 8), photo=random_photo(),
                       nickname=random_string("nickname", 5),
                       title=random_string("title", 4), company=random_string("company", 10),
                       address=random_address("address", 20),
                       home=random_number(9), mobile=random_number(9), work=random_number(9),
                       fax=random_number(9), email=random_email("email", 8), email2=random_email("email2", 8),
                       email3=random_email("email3", 8), homepage=random_website("homepage", 8), bday=random_day(),
                       bmonth=random_month(), byear=random_year(), aday=random_day(), amonth=random_month(),
                       ayear=random_year(), address2=random_address("address", 20), phone2=random_number(9),
                       notes=random_string("notes", 7))
               for i in range(5)
           ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
