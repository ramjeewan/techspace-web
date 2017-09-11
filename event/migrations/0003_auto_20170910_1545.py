# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-10 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_events_club'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='club',
            field=models.CharField(blank=True, choices=[('codeschool', 'Codeschool'), ('cogitans', 'Cogitans'), ('droidclub', 'Droid Club'), ('ecell', 'E-Cell'), ('electrotech', 'Electrotech'), ('oslc', 'OSLC'), ('renderedusict', 'Rendered-USICT'), ('turingai', 'Turing A.I.')], max_length=200),
        ),
    ]