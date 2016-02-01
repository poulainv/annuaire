# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20151129_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, default='', populate_from='title'),
            preserve_default=False,
        ),
    ]
