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
    
    data = pd.read_csv("./Data/DataSet.csv", header = 0)
    outputContinus(data)
    outputCategorical(data)
    
def outputContinus(data):
    #continusValue = pandas.DataFrame
    res = pd.DataFrame(data.as_matrix(["age", "fnlwgt", "capital-gain", "capital-loss", "hours-per-week"]), columns=["age", "fnlwgt", "capital-gain", "capital-loss", "hours-per-week"])
    switchContinuous(res)
    #py.iplot(res.ix[:,'age'], filename = 'test')
    '''res.plot(x=res.index,y='age')
    res.plot(x=res.index,y='fnlwgt')
    res.plot(x=res.index,y='capital-gain')
    res.plot(x=res.index,y='capital-loss')
    res.plot(x=res.index,y='hours-per-week')'''
    '''trace0 = go.Scatter(
        x=[1, 2, 3, 4],
        y=[10, 15, 13, 17]
    )
    trace1 = go.Scatter(
        x=[1, 2, 3, 4],
        y=[16, 5, 11, 9]
    )
    data = [trace0, trace1]
    
    py.plot(data, filename = 'basic-line')'''
    
    #res = res.describe()
    return res
    
    
def outputCategorical(data):
    res = pd.DataFrame(data.as_matrix(["workclass","education","education-num","marital-status","occupation","relationship","race","sex"]), columns=["workclass","education","education-num","marital-status","occupation","relationship","race","sex"] )
    switchCategorical(res)
 
def getCardinality(data):
    return data.apply(pd.Series.nunique)

def switchContinuous(data):
    cardinalities = getCardinality(data)
    for key, cardinality in cardinalities.iteritems():
        if cardinality < 10:
            barPlot(data.as_matrix([key]))
        else:
            histogram(data.as_matrix([key]),data.index.values,key)
        
def switchCategorical(data):
    for key in list(data):
        barPlot(data.as_matrix([key]))
    
def histogram(data,index,key):
    plotly.tools.set_credentials_file(username='Thibot', api_key='8faf2ltiCOcQnqDoGq8y')
    plotly.tools.set_config_file(world_readable=True,sharing='public')
    
    layout = go.Layout(
    title=key,
    xaxis=dict(
        title='List of '+key,
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Number of iterations ',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
    )
    
    ToPlot =go.Figure(data=[go.Histogram(x=data,name=key)],layout=layout)
    
    
    py.plot(ToPlot, filename = key)
    
def barPlot(data):
    print("Hello")
    

main()