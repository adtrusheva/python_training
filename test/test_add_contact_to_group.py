from model.contact import Contact
from model.group import Group
from random import randrange
import allure


def test_add_contact_to_group(app, db, check_ui):
    old_contacts = given_non_empty_contact_list(app, db)
    groups = given_non_empty_group_list(app, db)
    index = random_contact_index(old_contacts)
    index_group = random_group_index(groups)
    group = groups[index_group]
    contact = old_contacts[index]

    check_group_without_contact(contact, group, app, db)

    add_contact_to_group(contact, group, app)
    contacts_in_group = contacts_in_groups(group, db)

    check_contact_in_group(contact, contacts_in_group)


@allure.step('Given a non-empty contact list')
def given_non_empty_contact_list(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    return db.get_contact_list()


@allure.step('Given a non-empty group list')
def given_non_empty_group_list(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    return db.get_group_list()


@allure.step('Given a random index contact from the list')
def random_contact_index(old_contacts):
    index = randrange(len(old_contacts))
    return index


@allure.step('Given a random index group from the list')
def random_group_index(groups):
    index_group = randrange(len(groups))
    return index_group


@allure.step('Given a contact list')
def given_contact_list(db):
    return db.get_contact_list()


@allure.step('Given a group list')
def given_group_list(db):
    return db.get_group_list()


@allure.step('Given a contact list from the group')
def contacts_in_groups(group, db):
    return db.get_contacts_in_group(group)


@allure.step('Given a group without this contact')
def check_group_without_contact(contact, group, app, db):
    if contact in contacts_in_groups(group, db):
        app.contact.delete_contact_from_group(contact, group.id)


@allure.step('I add a contacts to the group')
def add_contact_to_group(contact, group, app):
    app.contact.add_contact_to_group(contact, group.id)


@allure.step('Then a contact added in group contact list')
def check_contact_in_group(contact, contacts_in_group):
    assert contact in contacts_in_group
