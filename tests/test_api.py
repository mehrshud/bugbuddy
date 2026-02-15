import pytest
from api import API

@pytest.fixture
def api():
    return API()

def test_setup(api):
    assert api is not None

def test_get_issues(api, mocker):
    mocker.patch('api.requests.get', return_value={'issues': []})
    assert api.get_issues() == []

def test_create_issue(api, mocker):
    mocker.patch('api.requests.post', return_value={'issue': {}})
    assert api.create_issue('Title', 'Description') == {}

def test_create_issue_invalid_data(api):
    with pytest.raises(ValueError):
        api.create_issue(None, None)

def test_get_issue(api, mocker):
    mocker.patch('api.requests.get', return_value={'issue': {}})
    assert api.get_issue(1) == {}

def test_get_issue_not_found(api, mocker):
    mocker.patch('api.requests.get', return_value=None)
    with pytest.raises(ValueError):
        api.get_issue(1)
