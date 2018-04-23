# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 21:49:39 2018

@author: Thibaut
"""

import csv

def main():
    array = []
    rows  = csv.reader(open("DataSet.csv","r"))
    
    for row in rows:
        temp = []
        for value in row:
            temp.append(value)
        array.append(temp)
    del array[0]
    
    writer = csv.writer(open("./data/team-name-DQR-ContinuousFeatures.csv", "wb"))
   
    for row in array:
        print(row)  
        writer.writerow(row)
                


if _name_ == "_main_":
    main()