# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20151124_0914'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name_plural': 'sub_categories'},
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=s3direct.fields.S3DirectField(default='https://pbs.twimg.com/profile_images/501725297729757184/wAYAzoPo.png'),
            preserve_default=False,
        ),
    ]
