# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20151123_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='category',
        ),
        migrations.AddField(
            model_name='project',
            name='categories',
            field=models.ManyToManyField(to='app.Category', related_name='projectos'),
        ),
        migrations.AddField(
            model_name='project',
            name='sub_categories',
            field=models.ManyToManyField(to='app.Category', related_name='projects'),
        ),
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
