from model.contact import Contact
import random
import string

constant = [
    Contact(
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
    ),
    Contact(
        photo='contact_photo.jpg',
        firstname='Test',
        middlename='Test2',
        lastname='Test3',
        nickname='Test44',
        title='fun',
        company='SelfTest',
        address='Moscow, Color Test Bulvar',
        home='981747284',
        mobile='983006475',
        work='9200737264',
        fax='8473740094',
        email='4Test662e@mail.ru',
        email2='6Test3g73mail.ru',
        email3='fTestgr63hf@mail.ru',
        homepage='terwyeTest.com',
        bday='12',
        bmonth='May',
        byear='1997',
        aday='6',
        amonth='June',
        ayear='1999',
        address2='Moscow, Red Test Bulvar',
        phone2='920003627',
        notes='portTest'
    )
]


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