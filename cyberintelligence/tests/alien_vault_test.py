from django.test import TestCase
from ..models.alien_vault import AlienVault
from django.conf import settings

class AlienVaultTestCase(TestCase):
    def setUp(self):
        self.av = AlienVault(settings.ALIEN_VAULT_API_KEY)

    def test_make_ip_query(self):
        self.assertTrue(isinstance(self.av.make_ip_query('8.8.8.8'), dict), "'response' is a dict class")
        self.assertRaises(Exception, lambda: self.av.make_ip_query('google.com'))

    def test_make_domain_query(self):
        self.assertTrue(isinstance(self.av.make_domain_query('google.com'), dict), "'response' is a dict class")
        self.assertRaises(Exception, lambda: self.av.make_domain_query('8.8.8.8'))
