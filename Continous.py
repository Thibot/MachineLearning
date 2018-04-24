# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 17:37:28 2018

@author: Thibaut
"""

class Categorical:
    
    def __init__(self,data=[]):
        self.Dataframe = data
        
    def Cardinality(self):
        return self.Dataframe.apply(pd.Series.nunique)