# -*- coding: utf-8 -*-

from urllib import urlopen
from BeautifulSoup import BeautifulStoneSoup

class CMainManager(object):
    def __init__(self, data):
        self.__data = data
        self.result = False
        self.massage = u'Some error'

    def _get_url(self):
        return "http://google.com"

    def get_content(self):
        content = urlopen(self.__data).read()
        return BeautifulStoneSoup(content).find('body')

    def __cleare(self):
        pass