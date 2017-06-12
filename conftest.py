import pytest
from fixture.application import Application

wd = None


@pytest.fixture
def app(request):
    global wd
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    if wd is None:
        wd = Application(browser=browser, base_url=base_url)
    else:
        if not wd.is_valid():
            wd = Application(browser=browser, base_url=base_url)
    wd.session.ensure_login(username="admin", password="secret")
    return wd


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        wd.session.ensure_logout()
        wd.destroy()

    request.addfinalizer(fin)
    return wd


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
