from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from web_analyzer import settings

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
    'extract_pulsedive_task': {
        'task': 'cyberintelligence.tasks.extract_pulsedive',  # Cambia 'ruta.a.tu.extract_virus_total' a la ruta correcta de tu tarea
        'schedule': crontab(hour=20, minute=56),  # ejecutar todos los días a las 22:00
        'args': (path_blacklist_domain,),
    },
    'extract_virus_total_task': {
        'task': 'cyberintelligence.tasks.extract_virus_total',  # Cambia 'ruta.a.tu.extract_virus_total' a la ruta correcta de tu tarea
        'schedule': crontab(hour=21, minute=50),  # ejecutar todos los días a las 22:00
        'args': (path_blacklist_domain,),
    },
}