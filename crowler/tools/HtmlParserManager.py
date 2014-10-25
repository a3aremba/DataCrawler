# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
from urllib import urlopen
from crowler.models import RelevantWords


class HtmlParseManager(object):

    def __init__(self, siteConfigObject):
        self._siteConfigObject = siteConfigObject
        self._content = ''
        self._texts = []
        self.fillContent()
        self.get_clear_text_from_tags()
        self._list_reletive_words = []

    def fillContent(self):
        # f = open('testFileHtml', 'r+')
        # self._content = f.read()
        # url = "http://en.wikipedia.org/wiki/Prague"
        # self._content = urlopen(url).read()
        self._content = self._siteConfigObject.html_content
        self._texts = BeautifulSoup(self._content).findAll(text=True)

    def format_parent_line(self, element):
        parent_line = []
        for parent in element.findParents():
            if parent.name == '[document]':
                continue
            parent_line.append(parent.name)

        return '->'.join(str(e) for e in reversed(parent_line))

    def get_clear_text_from_tags(self):
        data_list = []
        for text in self._texts:
            words = str(text).strip()
            words = words.replace('\n', '')
            parent = self.format_parent_line(text)

            if not words or not parent:
                continue

            current_dict = {
                'content': words,
                'parent': parent
            }
            data_list.append(current_dict)
        self._texts = data_list

    def replace_all(self, text):
        dic = {'.': ' ',
               ',': ' ',
               ':': ' ',
               ';': ' '}
        for i, j in dic.iteritems():
            text = text.replace(i, j)
        return text

    def split_by_words(self, text):
        text = self.replace_all(text)
        text = text.split(' ')
        return text

    def format_answer_dict(self, list_of_words, data_dict):
        return_list = []
        for current_word in list_of_words:
            if not current_word:
                continue
            relevantword = {'siteConfig': '',
                            'word': current_word,
                            'tag_history': data_dict.get('parent')}
            return_list.append(relevantword)
        return return_list

    def make_list_of_words(self):
        list_of_relevand_words = []
        for current_dict in self._texts:
            relevand_words = self.format_answer_dict(self.split_by_words(current_dict.get('content')),
                                                     current_dict)
            for word in relevand_words:
                list_of_relevand_words.append(word)
        self._list_reletive_words = list_of_relevand_words
        return list_of_relevand_words

    def save_words_to_db(self):
        try:
            for save_dict in self._list_reletive_words:
                save_dict['siteConfig'] = self._siteConfigObject
                revWord = RelevantWords(**save_dict)
                revWord.save()
        except Exception, e:
            print str(e)
            return False

        return True


