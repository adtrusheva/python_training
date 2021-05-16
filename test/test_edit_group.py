# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange
import allure


def test_edit_some_group(app, db, check_ui):
    old_groups = given_non_empty_group_list(app,db)
    index = random_group_index(old_groups)
    group = given_updated_group_by_index(old_groups, index)
    edit_group(app, group)
    new_groups = given_group_list(db)
    check_groups(app, db, old_groups, group, index, check_ui)


@allure.step('Given a non-empty group list')
def given_non_empty_group_list(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    return db.get_group_list()


@allure.step('Given a random group index from the list')
def random_group_index(groups):
    index = randrange(len(groups))
    return index


@allure.step('Given a updated group by index to the list')
def given_updated_group_by_index(groups, index):
    group = Group(name="New1 group", footer="New1 footer", header="New1 header")
    group.id = groups[index].id
    return group


@allure.step('Given a group list')
def given_group_list(db):
    return db.get_group_list()


@allure.step('When I edit the group "{group}" from the list')
def edit_group(app, group):
    app.group.edit_group_by_id(group, group.id)


@allure.step('When I delete the group "{group}" from the list')
def delete_group(app, group):
    app.group.delete_group_by_id(group.id)


@allure.step('Then the new group list is equal to the old list with the edited group')
def check_groups(app, db, old_groups, group, index, check_ui):
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

