# -*- coding: utf-8 -*-
'''
Created on Feb 24, 2014

@author: denis
'''

def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

