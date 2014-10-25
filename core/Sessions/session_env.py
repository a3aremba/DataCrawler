# -*- coding: utf-8 -*- 

# from django.contrib.sessions.models import Session
# from django.contrib.sessions.backends.db import SessionStore
from redis_sessions.session import SessionStore
from django.utils.timezone import utc
import datetime
import logging
logger = logging.getLogger('core')

class SessionEnv(object):
    def __init__(self, sessionId):
        self.store = SessionStore(sessionId)
        self.sessionId = sessionId
        
    def setParam(self, key, value):
        self.store[key] = value
    
    def getParam(self, key, default=''):
        return self.store.get(key, default)
    
    def isSessionKeyExists(self):
        return self.store.exists(self.sessionId) 
        
    def isNewSession(self, new_sid):
        if self.store.load().get('sid') == new_sid:
            return False
        else:
            return True
    
    def getSesKey(self):
        return self.store.session_key
    
    def saveParam(self):
        self.store.save()
    
    def removeSession(self):
        self.store.delete(self.sessionId)
    
    def createNewSession(self):
        if not self.store.session_key:
            self.store.create()
        else:
            self.store.save()