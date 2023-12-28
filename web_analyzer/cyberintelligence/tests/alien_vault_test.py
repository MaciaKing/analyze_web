from django.test import TestCase
from cyberintelligence.classes.alien_vault import AlienVault
from django.conf import settings

class AlienVaultTestCase(TestCase):
    def setUp(self):
        self.av = AlienVault(settings.ALIEN_VAULT_API_KEY)

    def test_make_ip_query(self):
        self.assertTrue(isinstance(self.av.make_ip_query('google.com'), dict), "'response' is a dict class")