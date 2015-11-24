# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151018_1604'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='small_description',
            new_name='description',
        ),
        migrations.AddField(
            model_name='project',
            name='slogan',
            field=models.CharField(max_length=50, default='New slogan'),
            preserve_default=False,
        ),
    ]
