# Generated by Django 2.2.6 on 2019-11-04 20:00

from django.db import migrations

# Note: This migration was throwing exceptions so all of the fields/etc were removed.
# The table gets deleted later in 0006_delete_filefilesystemexporter.py.


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20191104_2000'),
        ('file', '0003_auto_20191014_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileFileSystemExporter',
            fields=[],
        ),
    ]
