# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-03-01 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0022_remove_personaltimetable_time_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaltimetable',
            name='advisors',
            field=models.ManyToManyField(related_name='Advisors', to='student.Student'),
        ),
    ]
