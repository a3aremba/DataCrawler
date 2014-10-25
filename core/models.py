# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from crowler.tools.MainManager import CMainManager

class SiteConfig(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(('Site url'), max_length=255)
    name = models.CharField(('Site name'), max_length=120)
    html_content = models.TextField('Content', null=True, default=' ')
    date = models.DateTimeField('Дата', auto_now=False, auto_now_add=True,
                                      blank=True, default=timezone.now())

    class Meta:
        app_label = 'core'
        verbose_name_plural = 'Site config'

    def save(self):
        self.html_content = CMainManager(self.url).get_content()
        super(SiteConfig, self).save()
