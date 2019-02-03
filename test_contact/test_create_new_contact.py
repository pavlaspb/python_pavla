# -*- coding: utf-8 -*-

import pytest
from model_contact.contact import Contact
from fixture_contact.application_contact import Application_contact

@pytest.fixture
def app(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_create_new_contact(app):
    app.open_home_page()
    app.login(login="admin", password="secret")
    app.create_new_contact(Contact(firstname="Свидетель", lastname="ИзФрязино"))
    app.return_to_contacts_page()
    app.logout()