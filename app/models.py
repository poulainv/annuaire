#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.db import models
from django.db.models.signals import pre_save
from s3direct.fields import S3DirectField
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.db.models import Q


class CategoryManager(models.Manager):

    def get_by_natural_key(self, name):
        return self.get(name=name)


class Category(models.Model):

    objects = CategoryManager()

    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):

    name = models.CharField(max_length=20, unique=True)
    category = models.ForeignKey(Category, related_name='sub_categories')

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name_plural = "sub_categories"


class Project(models.Model):

    title = models.CharField(max_length=50, unique=True)
    slogan = models.CharField(max_length=250)
    description = models.TextField(max_length=1500)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    url = models.URLField(unique=True)
    image = S3DirectField(dest='imgs')
    released_date = models.DateTimeField(null=True, blank=True)
    draft = models.BooleanField(default=False)
    youtube_url = models.URLField(blank=True)
    vimeo_url = models.URLField(blank=True)
    twitter_url = models.CharField(max_length=50, blank=True)
    facebook_url = models.CharField(max_length=50, blank=True)
    categories = models.ManyToManyField(Category, related_name='projects')
    sub_categories = models.ManyToManyField(SubCategory,
                                            related_name='projects')
    contact_name = models.CharField(max_length=250, blank=True)
    contact_telephone = models.CharField(max_length=20, blank=True)
    contact_mail = models.EmailField(blank=True)
    blog_article_url = models.URLField(blank=True)

    def __str__(self):
        return self.title.capitalize()

    @classmethod
    def search(cls, query):
        q_title = Q(title__icontains=query)
        q_slogan = Q(slogan__icontains=query)
        q_category = Q(categories__name__icontains=query)

        return Project.objects.filter(q_title | q_slogan | q_category).all()


@receiver(pre_save, sender=Project)
def validate_sub_category(sender, instance, **kwargs):
    for sub_cat in instance.sub_categories.all():
        if sub_cat.category not in instance.categories.all():
            raise ValidationError('"%s" does not belong to any categories of this project' % sub_cat)
