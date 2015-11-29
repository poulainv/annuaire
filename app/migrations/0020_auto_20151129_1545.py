# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20151129_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
