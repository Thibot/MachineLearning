# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 21:49:39 2018

@author: Thibaut
"""
#df['Column_Name'].value_counts() <-- calcul la fréquence des données d'une colonne
import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from collections import Counter


def main():
    
    data = pd.read_csv("./Data/DataSet.csv", header = 0)
    print("\n"
          "|----------------------------------------------------------------|\n"
          "|------------Welcome on our machine learning project-------------|\n"
          "|-------Developped in Python 3.6 please check your release-------|\n"
          "|-------------------What do you want to do ? --------------------|\n"
          "|----------------------------------------------------------------|\n")

    line=""
    while(line!="0" and line!="1" and line!="2" and line!="3" and line!="4" and line!="5"):
        print("\n1 - Get continous features\n2 - Get categorical features\n0 - Exit\n")
        line = input("Your choice is : ")

    while(line!="0"):
        if line == "1":
            outputContinus(data)
        elif line == "2":
           outputCategorical(data)
            
        print("\n1 - Get continous features\n2 - Get categorical features\n0 - Exit\n")
        line = input("Your choice is : ")

    print("Bye")
    
    
    
def outputContinus(data):
    #continusValue = pandas.DataFrame
    res = pd.DataFrame(data.as_matrix(["age", "fnlwgt", "capital-gain", "capital-loss", "hours-per-week"]), columns=["age", "fnlwgt", "capital-gain", "capital-loss", "hours-per-week"])
    #switchContinuous(res)
    reportContinus(res)

def reportContinus(df):
    #df['Column_Name'].value_counts() <-- calcul la fréquence des données d'une colonne
    miss = []
    for key in df:
        miss.append(df[key].tolist().count(" ?")/df[key].count()*100)
    df = df.describe().transpose()
    df['miss'] = miss
    print(df)
    #print(df['occupation'].tolist().count(" ?"))
    
def reportCategorical(df):
    #df['Column_Name'].value_counts() <-- calcul la fréquence des données d'une colonne
    miss = []
    for key in df:
        miss.append(df[key].tolist().count(" ?")/df[key].count()*100)
    df = df.describe().transpose()
    df['miss'] = miss
    print(df)
    #print(df['occupation'].tolist().count(" ?"))
    
def outputCategorical(data):
    res = pd.DataFrame(data.as_matrix(["workclass","education","education-num","marital-status","occupation","relationship","race","sex"]), columns=["workclass","education","education-num","marital-status","occupation","relationship","race","sex"] )
    switchCategorical(res)
    reportCategorical(res)
 
def getCardinality(data):
    return data.apply(pd.Series.nunique)

def switchContinuous(data):
    cardinalities = getCardinality(data)
    for key, cardinality in cardinalities.iteritems():
        if cardinality < 10:
            barPlot(data.as_matrix([key]),data.index.values,key)
        else:
            histogram(data.as_matrix([key]),data.index.values,key)
        
def switchCategorical(data):
    for key in list(data):
        barPlot(data.as_matrix([key]),key)
    
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
    
    
    plotly.offline.plot(ToPlot, filename = './Plots/Histogram/'+key)
    
def barPlot(data,name):
    plotly.tools.set_credentials_file(username='Thibot', api_key='8faf2ltiCOcQnqDoGq8y')
    plotly.tools.set_config_file(world_readable=True,sharing='public')
    
    layout = go.Layout(
    title=name,
    xaxis=dict(
        title='List of '+name,
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

    values={}
    for value in data:
        if value[0] in values:
            values[value[0]]+=1
        else:
            values[value[0]]=1
            
    X=[]
    Y=[]
    for key,value in values.items():
        X.append(key)
        Y.append(value)
        
    trace=go.Bar(
            x=X,
            y=Y,
            name=name
            )
    
    data=[trace]
    
    ToPlot =go.Figure(data=data,layout=layout)
    
    
    plotly.offline.plot(ToPlot, filename = './Plots/Bar/'+name)
    

main()