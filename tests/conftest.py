"""Defines fixtures available to all tests."""

import pytest
from webtest import TestApp

from notifyme.app import create_app
from notifyme.config import TestingConfig


@pytest.fixture
def app():
    """Application for the tests."""
    _app = create_app(TestingConfig)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture
def testapp(app):
    """A Webtest app."""
    return TestApp(app)
