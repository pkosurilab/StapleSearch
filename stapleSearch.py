#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 23:37:07 2022

@author: RyanFantasia
"""
import pandas as pd
# printing original string
def stapSearch(seq,toSearch,K):
    test_str=seq
    print("The original string is : " + str(test_str))
    #sub strings 
    res = [test_str[i: j] for i in range(len(test_str)) for j in range(i + 1, len(test_str) + 1) if len(test_str[i:j]) == K]

    #Assignments 
    j=0
    match = pd.DataFrame()

    for i in range (len(res)):
        match[i]=toSearch['Sequence'].str.contains(res[i])
        match_count=toSearch['Sequence'].str.contains(res[i]).sum()
        if match_count>0:
            print('substring: '+res[i]+' matches staples: '+str(match.index[match[i]].tolist()))
            #print ("There are {m} matches in staples with ".format(m=match_count)+ str(K)+ " substrings length"+" subsequence:"+res[i])
            j=j+1
    if j==0:
        print("No Matches of "+ str(K)+ " substring length")