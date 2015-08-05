import pytest
from flask import Flask
from flask_simpleldap import LDAP
from config import BaseConfig


@pytest.fixture(scope='class')
def app(request):
    '''A Flask application object with an automatically pushed context
    It is also configured by the BaseConfig object
    The scope for this is class, so we don't create an expensive object for simple tests
    '''
    app = Flask(__name__)
    app.config.from_object(BaseConfig)

    # Push the context so it can be used by the tests
    ctx = app.app_context()
    ctx.push()

    # Pop the context when we are finished
    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope='class')
def ldap(app):
    '''The flask_simpleldap object with the proper initialization ready to be used
    The scope for this is class, so we don't create an expensive object for simple tests
    '''
    ldap = LDAP(app)
    return ldap
