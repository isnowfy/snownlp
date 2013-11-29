# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
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
