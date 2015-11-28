# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20151124_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='blog_article_url',
            field=models.URLField(blank=True),
        ),
    ]
