# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-26 10:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quaker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='seen_by_admin',
            new_name='seen',
        ),
    ]