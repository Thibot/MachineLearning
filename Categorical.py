# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:58:36 2018

@author: Thibaut
"""

import panda as pd

class Categorical:
    
    def __init__(self,data=[]):
        self.Dataframe = data
        
    def Cardinality():
        self.Dataframe.apply(pd.Series.nunique)
        
    