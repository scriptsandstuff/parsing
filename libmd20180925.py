#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 08:40:25 2018

@author: m
"""
import re


"""
multisplit ...to split string s on multiple multi-char delims 
input: 
  s: string
  delims: a regex capturing group of alternatives
output:
  list of split strings
"""
# ==================================================================
# multisplit ...to split string s on multiple multi-char delims 
# input: 
#   s: string
#   delims: list of strings used to do splitting
# output:
#   list of split strings
# ==================================================================
def multisplit(s, delims):
    # replace current \n with something that will not otherwise appear
    # a leter cause avoid pain, G cause higher that F, hex
    s = s.strip('\n')
    s = re.sub('\n', 'GGGGGG', s)
    for d in delims:        
        if d == '.':
            s = re.sub(r'\.', '\n', s)
        else:
            s = re.sub(d, '\n', s)
    return [re.sub('GGGGGG', '\n', split) for split in s.splitlines()]

"""
"""
def multisplitCaptures(s, delims):
# ==================================================================
# multisplit ...to split string s on multiple multi-char delims 
# input: 
#   s: string
#   delims: a regex capturing group of alternatives
# output:
#   list of split strings
# ==================================================================
    for d in delims:
        s = re.sub(d[0], '\n', s)
        # ==============================================================
        # replace with newline and afterwards split the lines
        # ...cause we don't know a better way
        # ==============================================================
        # print(d)
    return s.splitlines()

"""
"""
def err(s):
    print("\n\n-----------------------------\n\t---", 
          s, "---\nfailed...Exitting\n\n")
    sys.exit()

"""
"""
def getch(s):
    return re.match('^.', s).group()

"""
"""
def trimList(l):
    if l[len(l) - 1] == '':
        l = l[:len(l) - 1]
    return l
