# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20151123_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='contact_mail',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='contact_name',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='contact_telephone',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
