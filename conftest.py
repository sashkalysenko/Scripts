import pytest
from fixture.application import Application

wd = None


@pytest.fixture
def app(request):
    global wd
    if wd is None:
        wd = Application()
    else:
        if not wd.is_valid():
            wd = Application()
    wd.session.ensure_login(username="admin", password="secret")
    return wd


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        wd.session.ensure_logout()
        wd.destroy()

    request.addfinalizer(fin)
    return wd
