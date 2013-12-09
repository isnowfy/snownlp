# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import re
import codecs

from . import zh

stop_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'stopwords.txt')
pinyin_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'pinyin.txt')
stop = set()
pinyin = {}
fr = codecs.open(stop_path, 'r', 'utf-8')
for word in fr:
    stop.add(word.strip())
fr.close()
fr = codecs.open(pinyin_path, 'r', 'utf-8')
for word in fr:
    words = word.split()
    pinyin[words[0]] = words[1:]
fr.close()


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


def get_pinyin(word):
    if word in pinyin:
        return pinyin[word]
    ret = []
    for w in word:
        if w in pinyin:
            ret += pinyin[w]
    return ret
