# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-13 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobmanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateuser',
            name='file',
            field=models.FileField(null=True, upload_to='candidate_cv', verbose_name='CV\xa0File'),
        ),
    ]
