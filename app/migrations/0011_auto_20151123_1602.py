# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20151123_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='categories',
            field=models.ManyToManyField(to='app.Category', related_name='projects'),
        ),
        migrations.AlterField(
            model_name='project',
            name='sub_categories',
            field=models.ManyToManyField(to='app.SubCategory', related_name='projects'),
        ),
    ]
