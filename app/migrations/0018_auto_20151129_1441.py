# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20151129_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='vimeo_identifier',
            field=models.CharField(blank=True, max_length=20, help_text='Fournir l\'identifiant videmo situé, par exemple "112137027" dans "https://vimeo.com/112137027". Attention la vidéo Youtube est affichée prioritairement si deux identifiants sont fournit.'),
        ),
    ]
