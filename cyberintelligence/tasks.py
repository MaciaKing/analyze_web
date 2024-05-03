from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.conf import settings
from .models.virus_total import VirusTotal
from .models.alien_vault import AlienVault
from .models.pulsedive import Pulsedive
from .models.last_line_read import LastLineRead
from .models.data_extracted import DataExtracted
from time import sleep
import datetime
import pdb


@shared_task(soft_time_limit=None)
def extract_pulsedive(file):
    """ Save extracted data to database.
    Params:
        - file (string). Is the path to the file. Represents a file with a 
        domains to be analyzed.

    Functionality:
        - This function is to extract data from the Pulsedive API.
        It reads a file where there are different domains to be analyzed and 
        saves the results obtained by the API in a local database.

    Returns:
        - None.
    """
    #pdb.set_trace()
    # Detect if the file is whitelisted
    white_list = is_white_list(file)

    pd = Pulsedive.objects.first()
    # if the first object does not exist, create a new one
    if pd is None:
        pd = Pulsedive()
    pd.last_day_used = datetime.datetime.now() # Set last day used to today
    pd.save()

    domains = read_file(file)

    error_in_petition = False # If in the query there are some kind of error then stop
    actual_requests = 0
    while pd.can_make_query(actual_requests) and not error_in_petition:
        print(f"Actual request = {actual_requests}")
        last_line_read = LastLineRead.objects.get(id=1).last_line_read_pulsedive
        try:
            response = pd.query(domains[last_line_read]) # Return dict
        except:
            error_in_petition=True
        save_data("Pulsedive", domains[last_line_read], response, white_list, (last_line_read + 1))

        # Pulsedive control
        actual_requests += 1
        pd.add_one_to_total_querys_on_month()
        sleep(pd.TIME_BETWEEN_REQUESTS)
    

@shared_task
def extract_alien_vault(file):
    #av = AlienVault(settings.ALIEN_VAULT_API_KEY)
    #domains = read_file(file)
    # c= settings.last_line_read_alien_vault
    # for i in c..c + av.max_operations
    #   av.read
    return file


@shared_task(soft_time_limit=None)
def extract_virus_total(file):
    """ Save extracted data to database.
    Params:
        - file (string). Is the path to the file. Represents a file with a 
        domains to be analyzed.

    Functionality:
        - This function is to extract data from the Virus Total API.
        It reads a file where there are different domains to be analyzed and 
        saves the results obtained by the API in a local database.

    Returns:
        - None.
    """
    white_list = is_white_list(file)

    vt = VirusTotal(settings.VIRUS_TOTAL_API_KEY)
    wait_time_between_requests = vt.get_waiting_time_between_requests()
    max_request_per_day = vt.get_MAX_REQUEST_PER_DAY()

    last_line_read_vt = LastLineRead.objects.first().last_line_read_virus_total
    domains = read_file(file)
    error_in_petition = False # if the key has been used on more, could be error

    while (max_request_per_day >= 0) and (not error_in_petition):
        print(f"max_request_per_day={max_request_per_day}") #, "last_line_read_vt = ", last_line_read_vt)
        try:
            response = vt.make_domain_query(domains[last_line_read_vt])
        except:
            error_in_petition = True # Excess of daily queries exceeded 
        save_data("Virus Total", domains[last_line_read_vt], response, white_list, last_line_read_vt)
        max_request_per_day = max_request_per_day - 1 # control the petitions
        last_line_read_vt = last_line_read_vt + 1 # get the next domain/ip 
        sleep(wait_time_between_requests) # Waiting time between querys


def save_data(extracted_from, domain, data_extracted, white_list, last_line_read):
    """ Save extracted data to database.
    Params:
        - extracted_from (string). Where the data is extracted from.
        - domain (string). The domain name.
        - data_extracted (json). Is the information extracted from extracted_from.
        - white_list (boolean). If the domain is white list or not.
        - last_line_read (integer). Save the last line read of the file.

    Functionality:
        - The functionality is to save data extracted from different apis. 
        For this we have 2 models: 
            DataExtracted saves the results of the domains.
            LastLineRead stores information about intelligence files.

    Returns:
        - None.
    """
    DataExtracted( extracted_from=extracted_from, domain=domain, data_extracted=data_extracted, white_list=white_list ).save()
    if extracted_from == "Virus Total":
        LastLineRead.objects.filter(id=1).update(last_line_read_virus_total=last_line_read) # Only have the first objcet for save the info
    elif extracted_from == "Pulsedive": 
        LastLineRead.objects.filter(id=1).update(last_line_read_pulsedive=last_line_read) # Only have the first objcet for save the info


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


def is_white_list(to_detect):
    """ Read a txt file.
    Params:
        - to_detect (string). Represents the file file_path .

    Functionality:
        - Return True if the filename contain whitelist.
    
    Returns:
        - (Boolean) Return True if the filename contain whitelist.
    """
    if "whitelist" in to_detect:
        return True
    return False
    