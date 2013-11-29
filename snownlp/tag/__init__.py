# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import codecs

from ..utils.tnt import TnT

data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         '199801.txt')
tagger = TnT()


def train(file_name):
    fr = codecs.open(file_name, 'r', 'utf-8')
    data = []
    for i in fr:
        line = i.strip()
        if not line:
            continue
        tmp = map(lambda x: x.split('/'), line.split())
        data.append(tmp)
    fr.close()
    tagger.train(data)

train(data_path)


def tag_all(words):
    return tagger.tag(words)


def tag(words):
    return map(lambda x: x[1], tag_all(words))
