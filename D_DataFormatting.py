# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 22:46:03 2018

@author: Thibaut
"""

import pandas as pd

#Function deleting a column in a dataframe
#DataFrame = dataframe object
#ColumnName = Name of the column to delete
#def delColumn(DataFrame,ColumnName):
    
#Function deleting a row in a dataframe
#DataFrame = dataframe object
#ColumnName = Name of the column to base deletion on
def delRow(DataFrame,ColumnName, value):
    DataFrame = DataFrame[DataFrame[ColumnName] != value]
    return DataFrame

def DATtoCSV(OriginFile,fileName,Columns):
    
    data = pd.read_csv(OriginFile,sep='\s+',names=Columns,na_values={"HeartRate": [" ?"],"Hand_Temperature": [" ?"],"Chest_Temperature": [" ?"],"Ankle_Temperature": [" ?"]},keep_default_na=False)
    
    data.to_csv(fileName,columns=Columns)
    
    print(fileName+"   :   Generated\n")