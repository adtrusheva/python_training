# -*- coding: utf-8 -*-
from model.group import Group
import random
import allure


def test_delete_some_group(app, db, check_ui):
    old_groups = given_non_empty_group_list(app, db)
    group = random_group(old_groups)
    delete_group(app, group)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == app.group.count()
    check_groups(app, old_groups, new_groups, group, check_ui)


@allure.step('Given a non-empty group list')
def given_non_empty_group_list(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    return db.get_group_list()


@allure.step('Given a random group from the list')
def random_group(groups):
    return random.choice(groups)


@allure.step('Given a group list')
def given_group_list(db):
    return db.get_group_list()


@allure.step('When I delete the group "{group}" from the list')
def delete_group(app, group):
    app.group.delete_group_by_id(group.id)


@allure.step('Then the new group list is equal to the old list with the deleted group')
def check_groups(app, old_groups, new_groups, group, check_ui):
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

