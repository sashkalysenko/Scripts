import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    wd = Application()
    request.addfinalizer(wd.destroy)
    return wd
