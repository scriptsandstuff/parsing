#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:01:18 2018

@author: m
"""

import pandas as pd
import numpy as np
import re as re
from constituencies_bin import r as r
# from constituencies_bin import *
# from libmd20180925 import *
import libmd20180925 as lmd

pd.options.display.max_colwidth = 30

def split_on_cty(s):
    rr = f'((and,? )?([Ii]n the|[Tt]he) {r.cty} of {r.ctyName2})+'
    ctyss = re.findall(rr, s)
    # ctyss is a list of tuples, make it a list of strings
    ctys = [cty[0] for cty in ctyss]
    # print(ctys)
    s = lmd.multisplit(s, ctys)
         
    d = pd.DataFrame()
    p = ' ,.;:\n'
    # ctyss is a list of tuples!!!!
    for i, cty in enumerate(ctyss):
        d = d.append(
                {
                        'cty': cty[3],
                        'ctyName': cty[4],
                        's': s[i+1].strip(p)
                        },
                ignore_index=True
                )
    return d

df = pd.read_csv('../data_tmp/schedule.csv')
d2 = pd.DataFrame()
d4 = pd.DataFrame()

for idx, row in df.iterrows():
    d2 = split_on_cty(row.Area)
    d2['con'] = row.Name
    
    d4 = pd.concat([d4, d2], ignore_index=True)
d4.set_index(['con', 'ctyName'], inplace=True)
d4
d4.to_csv('../data_tmp/schedule_multi-index_CTY_DF.csv')