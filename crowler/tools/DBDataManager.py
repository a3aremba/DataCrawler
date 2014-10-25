# -*- coding: utf-8 -*-

import datetime
from django.db import connection
from core.models import SiteConfig

class CDBDataManager(object):

    def __init__(self, url=None, name=None):
        self._status = False
        self._url = url
        self._name = name

    def getUrlList(self):
        return

    def saveUrl(self):
        if not self.__findUrlOnConfList(self._url):
            try:
                safeUrl = SiteConfig()
                safeUrl.url = self._url
                safeUrl.name = self._name
                safeUrl.save()
            except Exception, e:
                connection._rollback()
                if e.args[0] == 1062:
                    message = 'URL: '+str(self._url)+' - уже есть в базе'
                else:
                    message = 'Не удалось сохранить '+str(self._url)
                return False, message
            return True, None
        else:
            return True, 'Add any url on configuration list!'

    def __findUrlOnConfList(self, url):
        return True