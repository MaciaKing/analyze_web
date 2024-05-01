from django.test import TestCase
from ..models.pulsedive import Pulsedive
from django.conf import settings
import datetime

class PulsediveTestCase(TestCase):
    def setUp(self):
        self.pulsedive = Pulsedive()
    
    def test_make_domain_query(self):
        self.assertTrue(isinstance(self.pulsedive.query('google.com'), dict), "'response' is a dict class")

    def test_can_make_query(self):
        # Example 1
        # Can make querys
        self.pulsedive.last_day_used = datetime.datetime.now()
        self.pulsedive.total_querys_on_month = 40
        self.pulsedive.save()

        self.assertTrue(self.pulsedive.can_make_query(40) is True)
        
        # Example 2
        # Can make daily querys but not monthy
        # So must be false
        self.pulsedive.last_day_used = datetime.datetime.now()
        self.pulsedive.total_querys_on_month = 500
        self.pulsedive.save()

        self.assertTrue(self.pulsedive.can_make_query(40) is False)

        # Example 3
        # Same Example 2
        self.pulsedive.last_day_used = datetime.datetime.now()
        self.pulsedive.total_querys_on_month = 510
        self.pulsedive.save()

        self.assertTrue(self.pulsedive.can_make_query(40) is False)

        # Example 4
        # Max requests days is passed
        self.pulsedive.last_day_used = datetime.datetime.now()
        self.pulsedive.total_querys_on_month = 300
        self.pulsedive.save()

        self.assertTrue(self.pulsedive.can_make_query(50) is False)

        # Example 5
        # Max requests days is passed
        self.pulsedive.last_day_used = datetime.datetime.now()
        self.pulsedive.total_querys_on_month = 300
        self.pulsedive.save()

        self.assertTrue(self.pulsedive.can_make_query(51) is False)