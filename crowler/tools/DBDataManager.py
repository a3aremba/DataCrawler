# -*- coding: utf-8 -*-

import datetime
from django.db import connection
from core.models import SiteConfig

class CDBDataManager(object):

    def __init__(self, data):
        self._status = False
        self._dataDict = data

    def saveUrl(self):
        try:
            print self._dataDict
            safeUrl = SiteConfig()
            safeUrl.url = self._dataDict.get('url')
            safeUrl.name = self._dataDict.get('name')
            safeUrl.save()
        except Exception, e:
            connection._rollback()
            if e.args[0] == 1062:
                message = 'URL: '+str(self._url)+' - уже есть в базе'
            else:
                message = 'Не удалось сохранить '+str(self._url)
            return False, message
        return True, None
