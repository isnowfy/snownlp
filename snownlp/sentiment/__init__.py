# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from .. import normal
from .. import seg
from ..classification.bayes import Bayes

data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'sentiment.marshal')


class Sentiment(object):

    def __init__(self):
        self.classifier = Bayes()

    def save(self, fname):
        self.classifier.save(fname)

    def load(self, fname=data_path):
        self.classifier.load(fname)

    def handle(self, doc):
        words = seg.seg(doc)
        words = normal.filter_stop(words)
        return words

    def train(self, neg_docs, pos_docs):
        data = []
        for sent in neg_docs:
            data.append([self.handle(sent), 'neg'])
        for sent in pos_docs:
            data.append([self.handle(sent), 'pos'])
        self.classifier.train(data)

    def classify(self, sent):
        ret, prob = self.classifier.classify(self.handle(sent))
        if ret == 'pos':
            return prob
        return 1-prob


classifier = Sentiment()
classifier.load()


def classify(sent):
    return classifier.classify(sent)
