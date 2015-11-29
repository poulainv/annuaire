# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20151129_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='vimeo_url',
        ),
        migrations.AddField(
            model_name='project',
            name='vimeo_identifier',
            field=models.URLField(blank=True, help_text='Fournir l\'identifiant videmo situé, par exemple "112137027" dans "https://vimeo.com/112137027". Attention la vidéo Youtube est affichée prioritairement si deux identifiants sont fournit.', max_length=15),
        ),
        migrations.AlterField(
            model_name='project',
            name='youtube_identifier',
            field=models.CharField(blank=True, help_text='Fournir l\'identifiant youtube situé après "v=" dans l\'URL par exemple "2xegsh1CmPU" dans "https://www.youtube.com/watch?v=2xegsh1CmPU"', max_length=15),
        ),
    ]
