# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-06 19:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testingSystem', '0002_auto_20181106_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='right_answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='right', to='testingSystem.Variant'),
        ),
    ]