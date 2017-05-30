import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    wd = Application()
    request.addfinalizer(wd.destroy)
    return wd


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="asdasd", header="asdasdd", footer="dsafdas"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
