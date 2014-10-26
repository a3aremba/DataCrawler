# -*- coding: utf-8 -*-
from django.db import models
from core.models import SiteConfig

class RelevantWords(models.Model):
    id = models.AutoField(primary_key=True)
    siteConfig = models.ForeignKey(SiteConfig)
    site_name = models.CharField('Site name', null=True, default=' ', max_length=255)
    word = models.CharField('Word', max_length=255)
    tag_history = models.CharField('tag history', max_length=1024)

    class Meta():
        app_label = 'crowler'
        verbose_name_plural = 'Relevant Words'