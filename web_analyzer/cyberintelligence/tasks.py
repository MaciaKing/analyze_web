from __future__ import absolute_import, unicode_literals
from celery import shared_task
from time import sleep

@shared_task
def extract_alien_vault(file):
    sleep(5)
    return file


@shared_task
def extract_virus_total():
    None