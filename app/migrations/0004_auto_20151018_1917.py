# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20151018_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='creator',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
