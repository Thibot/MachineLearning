# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 22:46:03 2018

@author: Thibaut
"""

import numpy as np
import pandas as pd

#Function to read a .dat file and to return a double dimensions tab
#nameFile = path of the file
def readDATFile(nameFile):
    myarray = np.fromfile(nameFile,dtype=float,sep=' ')
    newArray = []
    ligne=[]
    for i in range(0,len(myarray)):
        ligne.append(myarray[i])
        if(i%54==0 and i!=0):
            newArray.append(ligne)
            ligne=[]

    return newArray

#Function deleting a column in a dataframe
#DataFrame = dataframe object
#ColumnName = Name of the column to delete
def delColumn(DataFrame,ColumnName):
    DataFrame.drop(ColumnName, axis=1, inplace=True)
    
#Function deleting a row in a dataframe
#DataFrame = dataframe object
#ColumnName = Name of the column to base deletion on
def delRow(DataFrame,ColumnName, value):
    DataFrame = DataFrame[DataFrame[ColumnName] != value]
    return DataFrame

def toCSV(values, fileName, columns):
    df = pd.DataFrame(values,
              columns = columns)
    
    df.to_csv("./" + fileName + ".csv")