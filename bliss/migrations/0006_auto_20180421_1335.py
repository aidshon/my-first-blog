# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-21 07:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bliss', '0005_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bliss.Genre'),
        ),
    ]