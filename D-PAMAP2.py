# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 20:00:54 2018

@author: Thibaut
"""
import numpy as np


def main():
    
    
    myarray = np.fromfile('./Data/PAMAP2_Dataset/Protocol/subject101.dat',dtype=float,count=55,sep=" ")
    
    for i in len(myarray):
        
    
    print(myarray)
main()