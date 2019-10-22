#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 13:19:11 2018

@author: m
"""

'''
    class r
    easy access to the many regexs
    why a class? not sure, I think maybe that 
    some editor or other gave tab completion for classes but not dictionaries
'''
class r:
    cty = r'(county|city|city and county)'    
    cty_name = r'([A-Z]\w+ [A-Z]\w+|[A-Z]\w+|[A-Z]\w+ [A-Z]\w+\-[A-Z]\w+)'    
    full_county = f'The {cty} of {cty_name}( and the {cty} of {cty_name})?\.'
    
    the = r'(the|that|those)'    
    ta = r'(that\ is|that\ are|which\ is|which\ are)'
    comp = r'compro?m?ised' # is that Freudian?
    win = r'(within|in)'
    
    minus = f'\,?\ ?except\ (for\ )?{the}\ parts?\ (thereof\ )?{ta}\ ({comp}\ )?{win} the constituenc(y|ies) of\ '    
    plus = r'^,? ?the electoral divisions? of:?(.*)'
    parts = f'(and )?{the}? ?parts? of the electoral divisions? of '
    partsplus = r'\,?\;?\n? ?and\,? (that|those)? parts? of the electoral divisions? of\:? '
    
    pplus = r'^,? ?the electoral divisions? of:?\n?\ ?'
    # former = r'in the former( Rural)? District of\;?\:?\n? ?'
    former = r' ?in the former ?'
    # r'(and )?(that|those) parts? of the electoral divisions? of'
    
    
    compas = r'(north|south|east|west)'
    # situated = r' (situated|that lies to the) ' # '{compas} of '
    situated = f' (situated|that lies to the) {compas} of (a line drawn along )?'
    
    
    conj = r'(\;|\:|\ and\ )'
    ws = r'(\w+|\,|\ )'
    # reLst = r'(\w+|\,|\ |St\.\s\w+\'\w)'
    lst = r'(\w+|\,|\ |St\.\ \w+.s)+'
    # st = r"(St\.\ \w+’\w)"
    st = r"(St\.\ \w+.s)"
    # possesive noun st. x's place
    # the issue is that the apostrophie is not a ' it is some other character '’'
    
    
    ctyName = r'(\w+\ ?\-?[A-Z]?\w+?\ ?\-?[A-Z]?\w+?)'
    ctyName2 = r'(\w+\ [A-Z]\w+\-[A-Z]?\w+|\w+\ [A-Z]\w+|\w+)'
    # rr = f'((and,? )?([Ii]n the|[Tt]he) {cty} of (\w+))+'
    # rr = f'((and,? )?([Ii]n the|[Tt]he) {cty} of {ctyName2})+'
    rr = f'((and,? )?([Ii]n the|[Tt]he) {cty} of {ctyName2})+'  

# partial eds:    
#     match:
#         'line drawn ' # df.iloc[19].Area is not captured
#         'M50'
# winner!!!!
#  list(df[df.Area.str.contains(r'parts? of the electoral divisions?')].Name) 
#  df.iloc[19] captured
 
 

    #
    #   the 'for' and 'thereof', in minus above, do not appear in a consistent manner
    #   indicating it was not in fact a computer that did the transcription
    #   comp = r'compro?m?ised' # is that Freudian?
    #   also it is absent on 1 occasion