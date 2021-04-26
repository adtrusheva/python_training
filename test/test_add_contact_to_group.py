from model.contact import Contact
from model.group import Group
from random import randrange


def test_add_contact_to_group(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))

    if app.group.count() == 0:
        app.group.create(Group(name="test"))

    old_contacts = db.get_contact_list()
    groups = db.get_group_list()
    index = randrange(len(old_contacts))
    index_group = randrange(len(groups))
    group = groups[index_group]
    contact = old_contacts[index]
    contacts_in_group = db.get_contacts_in_group(group)

    if contact in contacts_in_group:
        app.contact.delete_contact_from_group(contact, group.id)

    app.contact.add_contact_to_group(contact, group.id)
    contacts_in_group = db.get_contacts_in_group(group)

    assert contact in contacts_in_group
