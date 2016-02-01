# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_project_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
