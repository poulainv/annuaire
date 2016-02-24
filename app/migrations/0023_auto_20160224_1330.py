# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_project_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='sub_categories',
            field=models.ManyToManyField(related_name='projects', to='app.SubCategory', help_text='Le mieux est de sélectionner une sous catégorie appartenant à un catégorie du projet ;)', blank=True),
        ),
    ]
