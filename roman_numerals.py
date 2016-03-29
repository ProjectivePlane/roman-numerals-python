#!/usr/bin/python

import re

numerals={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
numeral_values=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
re_patterns=["^(M)(.*)$","^(CM)(.*)$","^(D)(.*)$","^(CD)(.*)$","^(C)(.*)$","^(XC)(.*)$","^(L)(.*)$","^(XL)(.*)$","^(X)(.*)$","^(IX)(.*)$","^(V)(.*)$","^(IV)(.*)$","^(I)(.*)$"]
re_values={"^(M)(.*)$":1000,"^(CM)(.*)$":900,"^(D)(.*)$":500,"^(CD)(.*)$":400,"^(C)(.*)$":100,"^(XC)(.*)$":90,"^(L)(.*)$":50,"^(XL)(.*)$":40,"^(X)(.*)$":10,"^(IX)(.*)$":9,"^(V)(.*)$":5,"^(IV)(.*)$":4,"^(I)(.*)$":1}

valid_roman_numeral_pattern="^[IVXLCDM]+$"

def toRomanNumeral(n):
    return numerals[n]

def toRoman(n):
    split_number=splitNumber(n)
    roman_digits=[toRomanNumeral(m) for m in split_number]
    return ''.join(roman_digits)

def splitNumber(n):
    m=n
    result=[]
    for v in numeral_values:
        while v<=m:
            m-=v
            result.append(v)
    return result

def toInteger(s):
    tmpString=s
    total=0
    for re_s in re_patterns:
        pattern=re.compile(re_s,re.IGNORECASE)
        while pattern.match(tmpString):
            match=pattern.match(tmpString)
            total+=re_values[re_s]
            tmpString=match.group(2)
    return total

def isValidRomanNumeral(s):
    pattern=re.compile(valid_roman_numeral_pattern,re.IGNORECASE)
    return pattern.match(s)

class InvalidRomanNumeral(ValueError):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)

class InvalidIntegerArgument(ValueError):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)
