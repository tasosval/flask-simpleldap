import pytest
from config import BaseConfig as Config
from flask_simpleldap import LDAPException


class TestWithDefaultParams:
    def test_login_with_AD(self, ldap):
        test = ldap.bind_user(Config.USER, Config.PASS)
        assert test is not None

    def test_login_for_unknown_user(self, ldap):
        test = ldap.bind_user(Config.USER + 'wrong', Config.PASS)
        assert test is None

    def test_login_for_bad_password(self, ldap):
        test = ldap.bind_user(Config.USER, Config.PASS + 'wrong')
        assert test is None


class TestWithDifferentParams:
    def test_login_without_AD(self, ldap):
        ldap.app.config['LDAP_CONNECT_ACTIVE_DIRECTORY'] = False
        with pytest.raises(LDAPException) as exc:
            test = ldap.bind_user(Config.USER, Config.PASS)
        assert 'Operations error' in str(exc.value)
        ldap.app.config['LDAP_CONNECT_ACTIVE_DIRECTORY'] = True

    def test_omiting_base_config_raises_errors(self, ldap):
        del ldap.app.config['LDAP_HOST']
        with pytest.raises(KeyError) as exc:
            test = ldap.bind_user(Config.USER, Config.PASS)
        assert 'LDAP_HOST' in str(exc.value)
        ldap.app.config['LDAP_HOST'] = Config.LDAP_HOST

        del ldap.app.config['LDAP_BASE_DN']
        with pytest.raises(KeyError) as exc:
            test = ldap.bind_user(Config.USER, Config.PASS)
        assert 'LDAP_BASE_DN' in str(exc.value)
        ldap.app.config['LDAP_BASE_DN'] = Config.LDAP_BASE_DN

        del ldap.app.config['LDAP_USERNAME']
        with pytest.raises(KeyError) as exc:
            test = ldap.bind_user(Config.USER, Config.PASS)
        assert 'LDAP_USERNAME' in str(exc.value)
        ldap.app.config['LDAP_USERNAME'] = Config.LDAP_USERNAME

        del ldap.app.config['LDAP_PASSWORD']
        with pytest.raises(KeyError) as exc:
            test = ldap.bind_user(Config.USER, Config.PASS)
        assert 'LDAP_PASSWORD' in str(exc.value)
        ldap.app.config['LDAP_PASSWORD'] = Config.LDAP_PASSWORD
