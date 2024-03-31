from __future__ import absolute_import, unicode_literals
import os
from datetime import timedelta
from celery import Celery
from celery.schedules import crontab
from web_analyzer import settings
import pdb

# Setup celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_analyzer.settings')
app = Celery('web_analyzer',
             broker_url = f"amqp://guest:guest@{os.environ.get('RABBITMQ_SERVER')}:5672//")
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.timezone = 'Europe/Madrid'

# Get file path for extract data
path_blacklist_domain = str(settings.BASE_DIR) + "/cyberintelligence/data_to_extract/blacklist_domain.txt"
path_whitelist_domain = str(settings.BASE_DIR) + "/cyberintelligence/data_to_extract/whitelist_domain.txt"



# Configurar tareas periódicas
app.conf.beat_schedule = {
    #'extract_alien_vault_task': {
    #    'task': 'cyberintelligence.tasks.extract_alien_vault',  # Cambia 'ruta.a.tu.extract_alien_vault' a la ruta correcta de tu tarea
        #'schedule': crontab(minute='*/2'),  # Ejecutar cada 2 minutos
    #    'schedule': timedelta(seconds=2),
    #    'args': ('periooodicaaaaa',),  # Argumentos de la tarea
    #} #,
    'extract_virus_total_task': {
        'task': 'cyberintelligence.tasks.extract_virus_total',  # Cambia 'ruta.a.tu.extract_virus_total' a la ruta correcta de tu tarea
        'schedule': crontab(hour=22, minute=00),  # ejecutar todos los días a las 22:00
        'args': (path_blacklist_domain,),
    },
}