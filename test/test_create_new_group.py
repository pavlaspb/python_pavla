# -*- coding: utf-8 -*-

import pytest
from model.group import Group
from fixture.application_group import Application_group

@pytest.fixture
def app(request):
    fixture = Application_group()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_create_new_group(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.create_new_group(Group(name="Pavla", header="header", footer="footer"))
    app.return_to_group_page()
    app.logout()

