from django.test import TestCase
from cyberintelligence.classes.pulsedive import Pulsedive
from django.conf import settings

class PulsediveTestCase(TestCase):
    def setUp(self):
        self.pulsedive = Pulsedive()
    
    def test_make_domain_query(self):
        self.assertTrue(isinstance(self.pulsedive.query('google.com'), dict), "'response' is a dict class")
