# -*- coding: utf-8 -*-
from model.group import Group
import allure


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = given_group_list(db)
    create_group(app, group)
    new_groups = given_group_list(db)
    check_groups(app, old_groups, new_groups, group, check_ui)


@allure.step('Given a group list')
def given_group_list(db):
    return db.get_group_list()


@allure.step('When I add the group "{group}" to the list')
def create_group(app, group):
    app.group.create(group)


@allure.step('Then the new group list is equal to the old list with the added group')
def check_groups(app, old_groups, new_groups, group, check_ui):
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert new_groups == app.group.get_group_list()
