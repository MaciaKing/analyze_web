# Generated by Django 4.2.4 on 2024-01-15 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LastLineRead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_line_read_alien_vault', models.IntegerField(default=0)),
                ('last_line_read_virus_total', models.IntegerField(default=0)),
            ],
        ),
    ]
