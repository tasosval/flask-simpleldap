class BaseConfig(object):
    USER = 'user@example.org'
    PASS = 'password'

    LDAP_HOST = 'ldap.example.org'
    LDAP_BASE_DN = 'OU=users,dc=example,dc=org'
    LDAP_USERNAME = 'CN=user,OU=Users,DC=example,DC=org'
    LDAP_PASSWORD = 'password'
    LDAP_CONNECT_ACTIVE_DIRECTORY = True
