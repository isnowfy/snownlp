# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

import seg as TnTseg

data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'data.txt')
segger = TnTseg.Seg()
segger.train(data_path)


def seg(sent):
    return list(segger.seg(sent))
