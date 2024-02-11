from __future__ import absolute_import, unicode_literals
import os
from datetime import timedelta
from celery import Celery
from celery.schedules import crontab
import pdb

# Setup celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_analyzer.settings')
app = Celery('web_analyzer',
             broker_url = f"amqp://guest:guest@{os.environ.get('RABBITMQ_SERVER')}:5672//")
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Configurar tareas periódicas
app.conf.beat_schedule = {
    'extract_alien_vault_task': {
        'task': 'cyberintelligence.tasks.extract_alien_vault',  # Cambia 'ruta.a.tu.extract_alien_vault' a la ruta correcta de tu tarea
        #'schedule': crontab(minute='*/2'),  # Ejecutar cada 2 minutos
        'schedule': timedelta(seconds=2),
        'args': ('periooodicaaaaa',),  # Argumentos de la tarea
    } #,
    #'extract_virus_total_task': {
    #    'task': 'ruta.a.tu.extract_virus_total',  # Cambia 'ruta.a.tu.extract_virus_total' a la ruta correcta de tu tarea
    #    'schedule': crontab(minute='*/2'),  # Ejecutar cada 2 minutos
    #},
}