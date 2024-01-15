from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.conf import settings
from cyberintelligence.classes.virus_total import VirusTotal
from cyberintelligence.classes.alien_vault import AlienVault
from time import sleep

@shared_task
def extract_alien_vault(file):
    av = AlienVault(settings.ALIEN_VAULT_API_KEY)
    domains = read_file(file)
    # c= settings.last_line_read_alien_vault
    # for i in c..c + av.max_operations
    #   av.read
    return file


@shared_task
def extract_virus_total():
    None

def read_file(file):
    """ Read a txt file.
    Params:
        - file (string). Represents the file to read.

    Functionality:
        - Read all file and saves all lines into list named 'lines'.
    
    Returns:
        - Returns a list of all lines read from the file.
    """
    with open(file) as f:
        lines = [line.rstrip() for line in f] # rstrip() ignores the final '\n' character
    return lines