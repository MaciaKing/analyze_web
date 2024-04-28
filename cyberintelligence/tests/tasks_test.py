# test_tasks.py
from django.test import TestCase
from django.conf import settings
from ..models.virus_total import VirusTotal
from ..models.alien_vault import AlienVault
from cyberintelligence.tasks import extract_alien_vault, extract_virus_total, save_data, read_file
from cyberintelligence.models import LastLineRead, DataExtracted

class TestTasks(TestCase):
    def setUp(self):
        # Cualquier configuración necesaria para las pruebas
        self.file_test = f"{settings.BASE_DIR}/cyberintelligence/tests/tasks_test_file.txt"
        self.file_test_solution = ["first line", "second line"]
        self.json = {"message": "testing"}
        self.domain = "google.com" 

    def test_extract_alien_vault(self):
        None

    def test_extract_virus_total(self):
        None

    def test_save_data(self):
        random_last_line_read = 20
        save_data("Virus Total", self.domain, self.json, True, random_last_line_read)

        # Should save only one record on database
        self.assertEqual(len(DataExtracted.objects.all()), 1)
        # Verifies that the domain has been extracted correctly
        self.assertEqual(DataExtracted.objects.get(domain=self.domain).domain, self.domain)
        # Verifies that the json has been saved correctly
        self.assertEqual(DataExtracted.objects.first().data_extracted, self.json)

        #  Verifies that is only one record of LastLineRead
        self.assertEqual(len(LastLineRead.objects.all()), 1)
        # Verifies last line read
        self.assertEqual(LastLineRead.objects.all().first().last_line_read_virus_total, 20)
        
        #  Verifies if I update the domain the json information has been changed
        save_data("Virus Total", self.domain, {"message":"new_json"}, True, random_last_line_read)
        # Should the same domain record
        self.assertEqual(len(DataExtracted.objects.all()), 1)
        # Should have different json
        self.assertNotEqual(DataExtracted.objects.first().data_extracted, self.json)

        # Save a different domain and there must be 2 record in the database
        save_data("Virus Total", "new domain", {"message":"new_json"}, True, random_last_line_read)
        self.assertEqual(len(DataExtracted.objects.all()), 2)


    def test_read_file(self):
        readed_test_file = read_file(self.file_test)
        # Verifies that the file read is the expected one
        self.assertEqual(readed_test_file, self.file_test_solution)


