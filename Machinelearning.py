# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 21:49:39 2018

@author: Thibaut
"""

import pandas as pd
import plotly
import plotly.plotly as py


def main():
    plotly.tools.set_credentials_file(username='Thibot', api_key='11kB7F8CkL70aJhZmmdA')
    plotly.tools.set_config_file(world_readable=True,sharing='public')
    
    data = pd.read_csv("./Data/DataSet.csv", header = 0)
    outputContinus(data)
    #outputCategorical(data)
    
def outputContinus(data):
    #continusValue = pandas.DataFrame
    res = pd.DataFrame(data.as_matrix(["age", "fnlwgt", "capital-gain", "capital-loss", "hours-per-week"]), columns=["age", "fnlwgt", "capital-gain", "capital-loss", "hours-per-week"])
    #py.iplot(res.ix[:,'age'], filename = 'test')
    '''res.plot(x=res.index,y='age')
    res.plot(x=res.index,y='fnlwgt')
    res.plot(x=res.index,y='capital-gain')
    res.plot(x=res.index,y='capital-loss')
    res.plot(x=res.index,y='hours-per-week')'''
    print(res.dtypes)
    trace0 = Scatter(
        x=res.index,
        y=res.ix[:,'age']
    )
    data = Data(trace0)
    
    py.plot(data, filename = 'basic-line')
    
def outputCategorical(data):
    res = pd.DataFrame(data.as_matrix(["workclass","fnlwgt","education","education-num","marital-status","occupation","relationship","race","sex"]), columns=["workclass","fnlwgt","education","education-num","marital-status","occupation","relationship","race","sex"] )
    print(res)
    

main()