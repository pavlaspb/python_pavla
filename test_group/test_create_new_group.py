# -*- coding: utf-8 -*-

import pytest
from model_group.group import Group
from fixture_group.application_group import Application_group

@pytest.fixture
def app(request):
    fixture = Application_group()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_create_new_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Pavla", header="header", footer="footer"))
    app.session.logout()