import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def driver(request):
    wd = Application()
    request.addfinalizer(wd.destroy)
    return wd


def test_add_group(driver):
    driver.login(username="admin", password="secret")
    driver.create_group(Group(name="asdasd", header="asdasdd", footer="dsafdas"))
    driver.logout()


def test_add_empty_group(driver):
    driver.login(username="admin", password="secret")
    driver.create_group(Group(name="", header="", footer=""))
    driver.logout()
