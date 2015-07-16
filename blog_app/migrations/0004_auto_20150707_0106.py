# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_auto_20150705_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(default='teste', unique=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default='teste2', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default='teste4', unique=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
