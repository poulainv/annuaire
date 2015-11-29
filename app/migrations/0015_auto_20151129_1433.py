# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_project_blog_article_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='youtube_url',
        ),
        migrations.AddField(
            model_name='project',
            name='youtube_identifier',
            field=models.CharField(blank=True, max_length=15, help_text='Fournir l\\identifiant youtube situé après "v=" dans l\'URL par exemple 2xegsh1CmPU dans "https://www.youtube.com/watch?v=2xegsh1CmPU"'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=s3direct.fields.S3DirectField(blank=True, help_text="Le ratio de l'image sera conservé. Préférez un format carré"),
        ),
        migrations.AlterField(
            model_name='project',
            name='sub_categories',
            field=models.ManyToManyField(to='app.SubCategory', related_name='projects', help_text='Le mieux est de sélectionner une sous catégorie appartenant à un catégorie du projet ;)'),
        ),
    ]
