from django.db import models
from django.dispatch import receiver # for the first insert
from django.db.models.signals import post_migrate # for the first insert

class LastLineRead(models.Model):
    last_line_read_alien_vault = models.IntegerField(default=0)
    last_line_read_virus_total = models.IntegerField(default=0)

    def get_model():
        return LastLineRead.objects.first()

@receiver(post_migrate)
def create_default_last_line_read(sender, **kwargs):
    if not LastLineRead.objects.exists():
        LastLineRead.objects.create()

class DataExtracted(models.Model):
    extracted_from = models.CharField(max_length=30, default='')
    domain = models.CharField(max_length=None, default='', primary_key=True)
    data_extracted = models.JSONField(default=dict) 
    white_list = models.BooleanField()