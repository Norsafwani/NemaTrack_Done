# Generated by Django 4.0 on 2021-12-17 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackApp', '0003_trackappdocument_delete_document'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TrackappDocument',
        ),
    ]
