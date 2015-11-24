# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20151123_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='facebook_url',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
