# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unicodedata
import logging
from django.conf import settings
from core.Sessions.session_env import SessionEnv
from core.webservices.promin.getParametersBySid.getParametersBySidInterface import CGetParametersBySidInterface
from core.webservices.promin.getAttrBySid.getAttrBySidInterface import CGetAttrBySidInterface

class SessionInfo:
    request = None

    def __init__(self, request):
        self.sessionId = None
        self.sid = None
        self.request = request
        if self.request.COOKIES.has_key('sessionid'):
            self.sessionId = self.request.COOKIES['sessionid']
#         if self.request.COOKIES.has_key('sid'):
#             self.sid = self.request.COOKIES.get('sid')
        if self.request.GET.has_key('sid'):
            try:
                self.sid = unicodedata.normalize('NFKD',
                                                 self.request.GET.get('sid')).encode('ascii','ignore')
            except:
                pass
        self.sessionEnv = SessionEnv(self.sessionId)
            
    def initFirstCall(self):
        if self.request.method != 'GET':
            self.logger.error('initFirstCall: self.request.method is invalid')
            return False

        if self.sessionEnv.isNewSession(self.sid):
            self.sessionEnv.removeSession()
            self.__createSessionParams()
        else:
            self.__createSessionParams()
        return True
    
    def __createSessionParams(self):
        branch = CGetParametersBySidInterface(self.sid).sendSession()
        attrBySid = CGetAttrBySidInterface(self.sid).sendSession()
        self.sessionEnv.setParam('sid', self.sid)
        self.sessionEnv.setParam('branch', branch)
        self.sessionEnv.setParam('sesParams', attrBySid.__dict__)
        self.sessionEnv.createNewSession()
        
    def getSesParams(self):
        return self.sessionEnv.getParam('sesParams')
         
    def getSid(self):
        return self.sessionEnv.getParam('sid')
    
    def getBranch(self):
        return self.sessionEnv.getParam('branch')
    
    def getSesKey(self):
        return self.sessionEnv.getSesKey()
    
    def setParam(self, key, value):
        self.sessionEnv.setParam(key, value)
        self.sessionEnv.saveParam()
    
    def getParam(self, key, default=''):
        return self.sessionEnv.getParam(key, default='')
    
    