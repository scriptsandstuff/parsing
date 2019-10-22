#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:29:37 2018

@author: m
"""

import pandas as pd
# import numpy as np
import re as re
from constituencies_bin import r
# from constituencies_dev import *
import libmd20180925 as md
pd.options.display.max_colwidth = 12

def parseParts(s1):
    '''
    Parse the string containing the magic words
    
    Parameters
    ----------
    s: String
        String to be parsed
    Returns
    -------
    []: array
        array of    1) list of affected eds, 
                    2) direction (as far as I remember)
                    3) description of boundary line
    Example
    -------
    >>> parseParts(s)
    [a, b, c]
    '''
    s1 = s1.strip(p)
    
    sits = re.findall(f'({r.situated})', s1) 
    # sits = re.search(r.situated, s1)           
    # sits = [sit[0] for sit in sits]
    sits = list(sits[0])
    # print(sits)   
                
    [part_eds, polylines]  = s1.split(sits[0])
    # [part_eds, polylines]  = s1.split(sits.group())
    # s1 = 'Glencullen that lies to the east of the M50 Motorway and to the south of the N31 and the Leopardstown Road'
    part_eds = md.multisplit(part_eds, [',', 'and'])
    part_eds = [pe.strip(p) for pe in part_eds]
    
    # print(sits[2])
    return [part_eds, sits[2], polylines]

def parsePlus(s):
    '''
    maybe have to parse the 'and' out of the last eds 
    '''
    # pplus = r'^,? ?the electoral divisions? of:?\n?\ ?' 
    s = re.sub(r.pplus, '', s)
    eds_lines_list = s.split('\n')
    
    a = {}
    a[''] = []
    for i, eds_line_str in enumerate(eds_lines_list):
        eds_line_str = eds_line_str.strip(p)
        # print(eds_line_str)
        # former = r' ?in the former ?'
        m = re.search(r.former, eds_line_str) 
        if m: # m = m[0]    # m = m.group()
            # split in 2 pieces: the eds list str and the district
            [s1, d] = eds_line_str.split(m[0])
            # strip spaces, split the str, 
            ll = s1.strip(p).split(',')
            # strip spaces again and make key district and value the list of eds
            a[d] = [lll.strip(p) for lll in ll]
        else:
            # print('no match')
            s1 = eds_line_str.strip(p)
            # if string starts with 'and' remove it
            s1 = re.sub('^ ?and ?', '', s1)
            ll = md.multisplit(s1, [',', ' and '])
            aa = [lll.strip(p) for lll in ll]
            a[''].extend(aa)
    return a

'''
'''
df = pd.read_csv('../../_dev_data/schedule_multi-index_CTY_DF.csv')

cols = ['ex_cons', 'eds_dicts', 'eds', 'eds_parts', 'direction', 'polylines']

d2 = pd.DataFrame(columns = cols)
d2 = d2.append(df)
d2.set_index(['con', 'ctyName', 'cty'], inplace=True)
# have 3rd index cause Cork city and Cork county
d2

p = ' ,.;:\n'
len_parts = 0

for j, cty in d2.iterrows():
    # print(cty)
    if cty.isna()['s']:
        continue
    
    s = cty.s
# =============================================================================
#     this should be done at the very beginning
# =============================================================================
    s = re.sub('\-\ ', '-', s)
            
    sminus = re.match(r.minus, s)
    if sminus:
        # parse the con and save till later
        c = re.sub(sminus.group(), '', s).strip(p)
        c = md.multisplit(c, [',', 'and'])
        c = [cc.strip(p) for cc in c]
        cty['ex_cons'] = c
        continue
    
    sparts = re.search(r.parts, s)
    if sparts:
        [s, s1] = s.split(sparts[0])  
        [a, b, c] = parseParts(s1)
        cty['eds_parts'] = a
        cty['direction'] = b
        cty['polylines'] = c
        # print(sparts[0])
        len_parts = len_parts + 1
        
    l = parsePlus(s)
    # del l[''] {'':[]} are those eds that were districts
    cty['eds_dicts'] = l
    
    ll = list(l.values()) # ll is a list of lists
    edl = []
    [edl.extend(lll) for lll in ll]
    # print(edl)
    
    cty['eds'] = edl

# d2.to_csv('../../_dev_data/schedule_DF.csv')
# to unpack eds_dicts to set of dictionaries lets use a json
d2.reset_index().to_json('../../_dev_data/schedule_DF.json')

# d3 = pd.read_json('../../_dev_data/schedule_DF.json')
# d3.set_index(['con', 'cty'], inplace=True)