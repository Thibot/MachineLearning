# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 21:49:39 2018

@author: Thibaut
"""

import pandas as pd

def main():
    data = pd.read_csv("./Data/DataSet.csv", header = 0)
    outputContinus(data)
    
def outputContinus(data):
    #continusValue = pandas.DataFrame
    i = 0
    for column in data:
        if i in [1, 3, 11, 12, 13]:
            print(data[i])
        i += 1
    
def outputCategorical(data):
    print()
    
main()