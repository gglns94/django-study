# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 15:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choicec',
            new_name='Choice',
        ),
    ]
