# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import re
import codecs

from . import zh
from . import pinyin

stop_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'stopwords.txt')
pinyin_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'pinyin.txt')
stop = set()
fr = codecs.open(stop_path, 'r', 'utf-8')
for word in fr:
    stop.add(word.strip())
fr.close()
pin = pinyin.PinYin(pinyin_path)


def filter_stop(words):
    return list(filter(lambda x: x not in stop, words))


def zh2hans(sent):
    return zh.transfer(sent)


def get_sentences(doc):
    line_break = re.compile('[\r\n]')
    delimiter = re.compile('[，。？！；]')
    sentences = []
    for line in line_break.split(doc):
        line = line.strip()
        if not line:
            continue
        for sent in delimiter.split(line):
            sent = sent.strip()
            if not sent:
                continue
            sentences.append(sent)
    return sentences


def get_pinyin(sentence):
    return pin.get(sentence)
