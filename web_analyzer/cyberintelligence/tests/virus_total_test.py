from django.test import TestCase
from cyberintelligence.classes.virus_total import VirusTotal
from django.conf import settings

class VirusTotalTestCase(TestCase):
    def setUp(self):
        self.vt = VirusTotal(settings.VIRUS_TOTAL_API_KEY) # better create another api key
    
    def test_make_ip_query(self):
        self.assertTrue(isinstance(self.vt.make_ip_query('8.8.8.8'), dict), "'response' is a dict class")
        self.assertRaises(Exception, lambda: self.vt.make_ip_query('google.com'))

    def test_make_domain_query(self):
        self.assertTrue(isinstance(self.vt.make_domain_query('google.com'), dict), "'response' is a dict class")
        self.assertRaises(Exception, lambda: self.vt.make_domain_query('8.8.8.8'))
