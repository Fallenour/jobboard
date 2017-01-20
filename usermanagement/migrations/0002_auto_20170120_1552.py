# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-20 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateuser',
            name='file',
            field=models.FileField(upload_to='candidate_cv', verbose_name='CV\xa0File'),
        ),
        migrations.AlterField(
            model_name='candidateuser',
            name='skill',
            field=models.CharField(blank=True, max_length=100, verbose_name='Candidate Skill'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='skill',
            field=models.CharField(blank=True, max_length=100, verbose_name='Researched Skill'),
        ),
    ]