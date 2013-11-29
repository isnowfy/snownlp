# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import bm25


class TextRank(object):

    def __init__(self, docs):
        self.docs = docs
        self.bm25 = bm25.BM25(docs)
        self.D = len(docs)
        self.d = 0.85
        self.weight = []
        self.weight_sum = []
        self.vertex = []
        self.max_iter = 200
        self.min_diff = 0.001
        self.top = []

    def solve(self):
        for doc in self.docs:
            scores = self.bm25.simall(doc)
            self.weight.append(scores)
            self.weight_sum.append(sum(self.weight[-1]))
            self.vertex.append(1.0)
        for _ in range(self.max_iter):
            m = []
            max_diff = 0
            for i in range(self.D):
                m.append(1-self.d)
                for j in range(self.D):
                    if j == i:
                        continue
                    m[-1] += (self.d*self.weight[i][j]
                              / self.weight_sum[j]*self.vertex[j])
                if abs(m[-1] - self.vertex[i]) > max_diff:
                    max_diff = abs(m[-1] - self.vertex[i])
            self.vertex = m
            if max_diff <= self.max_dif:
                break
        self.top = list(enumerate(self.vertex))
        self.top = sorted(self.vertex, key=lambda x: x[1], reverse=True)

    def top_index(self, limit):
        return map(lambda x: x[0], self.top)

    def top(self, limit):
        return map(lambda x: self.docs[x[0]], self.top)
