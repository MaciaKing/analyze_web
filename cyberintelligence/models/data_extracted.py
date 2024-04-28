from django.db import models

class DataExtracted(models.Model):
    extracted_from = models.CharField(max_length=30, default='')
    domain = models.CharField(max_length=None, default='', primary_key=True)
    data_extracted = models.JSONField(default=dict) 
    white_list = models.BooleanField()