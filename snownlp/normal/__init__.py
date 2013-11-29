# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import re
import codecs

import zh

data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'stopwords')
stop = set()
fr = codecs.open(data_path, 'r', 'utf-8')
for word in fr:
    stop.add(word.strip())
fr.close()


def filter_stop(words):
    return filter(lambda x: x not in stop, words)


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
