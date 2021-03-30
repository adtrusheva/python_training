# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit_first_group(Group(name="New1 group", footer="New1 footer", header="New1 header"))


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="02"))
    app.group.edit_first_group(Group(name="New Test"))


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="01"))
    app.group.edit_first_group(Group(header="New3 header"))