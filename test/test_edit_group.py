# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="New1 group", footer="New1 footer", header="New1 header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="02"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="New Test"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="01"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header="New3 header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)