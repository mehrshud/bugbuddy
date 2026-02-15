import pytest
from unittest.mock import Mock
from BugBuddy import BugBuddy

@pytest.fixture
def bug_buddy():
    return BugBuddy()

def test_init(bug_buddy):
    assert bug_buddy is not None

def test_positive_test_case(bug_buddy):
    assert bug_buddy.run() == True

def test_negative_test_case(bug_buddy):
    bug_buddy.mock_error = Mock(side_effect=Exception)
    with pytest.raises(Exception):
        bug_buddy.run()

def test_edge_case(bug_buddy):
    bug_buddy.config = None
    with pytest.raises(AttributeError):
        bug_buddy.run()

def test_mocks(bug_buddy):
    bug_buddy.dependency = Mock()
    bug_buddy.dependency.return_value = True
    assert bug_buddy.run() == True
