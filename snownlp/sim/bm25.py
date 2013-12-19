# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import math
from collections import defaultdict

class BM25(object):

    def __init__(self, docs):
        self.D = len(docs)
        self.avgdl = sum(map(lambda x: len(x)+0.0, docs)) / self.D
        self.docs = docs
        self.f = []
        self.df = defaultdict(int)
        self.idf = {}
        self.k1 = 1.5
        self.b = 0.75
        self.init()

    def init(self):
        for doc in self.docs:
            tmp = defaultdict(int)
            for word in doc:
                tmp[word] += 1
            self.f.append(tmp)
            for k, v in tmp.iteritems():
                self.df[k] += 1
        for k, v in self.df.iteritems():
            self.idf[k] = math.log(self.D-v+0.5)-math.log(v+0.5)

    def sim(self, doc, index):
        score = 0
        for word in doc:
            if word not in self.f[index]:
                continue
            score += (self.idf[word]*self.f[index][word]*(self.k1+1)
                      / (self.f[index][word]+self.k1*(1-self.b+self.b*self.D
                                                      / self.avgdl)))
        return score

    def simall(self, doc):
        scores = []
        for index in range(self.D):
            score = self.sim(doc, index)
            scores.append(score)
        return scores
