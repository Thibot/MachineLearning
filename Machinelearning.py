# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 21:49:39 2018

@author: Thibaut
"""

import pandas as pd

def main():
    data = pd.read_csv("./Data/DataSet.csv", header = 0)
    outputContinus(data)
    outputCategorical(data)
    
def outputContinus(data):
    #continusValue = pandas.DataFrame
    res = pd.DataFrame(data.as_matrix(["age", "fnlwgt", "capital-gain", "capital-loss", "hours-per-week"]), columns=["age", "fnlwgt", "capital-gain", "capital-loss", "hours-per-week"])
    res.plot(x=res.index,y='age')
    res.plot(x=res.index,y='fnlwgt')
    res.plot(x=res.index,y='capital-gain')
    res.plot(x=res.index,y='capital-loss')
    res.plot(x=res.index,y='hours-per-week')
    #print(res)
    
def outputCategorical(data):
    res = pd.DataFrame(data.as_matrix(["workclass","fnlwgt","education","education-num","marital-status","occupation","relationship","race","sex"]), columns=["workclass","fnlwgt","education","education-num","marital-status","occupation","relationship","race","sex"] )
    #print(res)
    

main()