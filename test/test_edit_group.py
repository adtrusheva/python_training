from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="566300", header="00000d", footer="999999w"))
    app.session.logout()