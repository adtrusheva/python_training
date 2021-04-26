from model.contact import Contact
from model.group import Group
from random import randrange


def test_del_contact_from_group(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))

    if app.group.count() == 0:
        app.group.create(Group(name="test"))

    groups = db.get_group_list()
    index_group = randrange(len(groups))
    group = groups[index_group]
    contacts = db.get_contacts_in_group(group)

    if len(contacts) == 0:
        contacts = db.get_contact_list()
        index = randrange(len(contacts))
        contact = contacts[index]
        app.contact.add_contact_to_group(contact, group.id)
    else:
        index = randrange(len(contacts))
        contact = contacts[index]

    app.contact.delete_contact_from_group(contact, group.id)

    contacts_in_group = db.get_contacts_in_group(group)

    assert contact not in contacts_in_group
