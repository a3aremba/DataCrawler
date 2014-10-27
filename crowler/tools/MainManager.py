# -*- coding: utf-8 -*-

from urllib import urlopen
from BeautifulSoup import BeautifulSoup

class CMainManager(object):
    def __init__(self, data):
        self.__data = data
        self.result = False
        self.massage = u'Some error'

    def get_content(self):
        content = urlopen(self.__data).read()
        return self.__cleare(BeautifulSoup(content).body)

    def __cleare(self, data):
        for tag in data.findAll(['script','style', 'iframe']):
            tag.replaceWith('')
        return data