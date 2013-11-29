# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import codecs

import tnt


class Seg(object):

    def __init__(self):
        self.segger = tnt.TnT()

    def train(self, file_name):
        fr = codecs.open(file_name, 'r', 'utf-8')
        data = []
        for i in fr:
            line = i.strip()
            if not line:
                continue
            tmp = map(lambda x: x.split('/'), line.split())
            data.append(tmp)
        fr.close()
        self.segger.train(data)

    def seg(self, sentence):
        ret = self.segger.tag(sentence)
        tmp = ''
        for i in ret:
            if i[1] == 's':
                yield i[0]
            elif i[1] == 'e':
                yield tmp+i[0]
                tmp = ''
            else:
                tmp += i[0]


if __name__ == '__main__':
    seg = Seg()
    seg.train('data.txt')
    print ' '.join(seg.seg('主要是用来放置一些简单快速的中文分词和词性标注的程序'))
