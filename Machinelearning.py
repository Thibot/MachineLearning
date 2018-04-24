# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 21:49:39 2018

@author: Thibaut
"""

import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go


def main():
    plotly.tools.set_credentials_file(username='Thibot', api_key='8faf2ltiCOcQnqDoGq8y')
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
    trace0 = go.Scatter(
        x=[1, 2, 3, 4],
        y=[10, 15, 13, 17]
    )
    trace1 = go.Scatter(
        x=[1, 2, 3, 4],
        y=[16, 5, 11, 9]
    )
    data = [trace0, trace1]
    
    py.plot(data, filename = 'basic-line')
    
    res = res.describe()
    
    
def outputCategorical(data):
    res = pd.DataFrame(data.as_matrix(["workclass","fnlwgt","education","education-num","marital-status","occupation","relationship","race","sex"]), columns=["workclass","fnlwgt","education","education-num","marital-status","occupation","relationship","race","sex"] )
    print(res)
    

main()