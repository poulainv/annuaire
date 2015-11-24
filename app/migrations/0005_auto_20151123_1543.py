# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20151018_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('category', models.ForeignKey(related_name='sub_categories', to='app.Category')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='facebook_url',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='released_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='twitter_url',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(default='www.foo.com'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='vimeo_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='youtube_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.ForeignKey(related_name='projects', to='app.Category'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='project',
            name='slogan',
            field=models.CharField(max_length=250),
        ),
    ]
