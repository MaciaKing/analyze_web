from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.conf import settings
from cyberintelligence.classes.virus_total import VirusTotal
from cyberintelligence.classes.alien_vault import AlienVault
from cyberintelligence.models import LastLineRead
from time import sleep
import pdb

@shared_task
def extract_alien_vault(file):
    av = AlienVault(settings.ALIEN_VAULT_API_KEY)
    domains = read_file(file)
    # c= settings.last_line_read_alien_vault
    # for i in c..c + av.max_operations
    #   av.read
    return file


@shared_task
def extract_virus_total(file):
    vt = VirusTotal(settings.VIRUS_TOTAL_API_KEY)
    wait_time_between_requests = vt.get_waiting_time_between_requests()
    #max_request_per_day = vt.get_MAX_REQUEST_PER_DAY()
    max_request_per_day = 5

    last_line_read_vt = LastLineRead.objects.first().last_line_read_virus_total
    domains = read_file(file)
    error_in_petition = False # if the key has been used on more, could be error

    while (max_request_per_day > 0) and (not error_in_petition):
        print(domains[last_line_read_vt])
        response = vt.make_domain_query(domains[last_line_read_vt])
        #virus_total_deque.append((domains[last_line_read_vt], response))
        
        max_request_per_day = max_request_per_day - 1 # control the petitions
        last_line_read_vt = last_line_read_vt + 1 # get the next domain/ip 
        pdb.set_trace()
    
    pdb.set_trace()

    
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