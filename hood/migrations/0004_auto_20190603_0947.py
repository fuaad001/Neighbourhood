# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-06-03 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0003_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Resident', 'Resident')], default='Resident', max_length=10),
        ),
    ]
