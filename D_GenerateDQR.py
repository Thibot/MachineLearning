# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 21:49:39 2018

@author: Thibaut
"""
__author__ = "Team D"
__credits__ = "Bastien Laise, Florian Hemery, Clément Croislebois and Thibaut Roudel"


#df['Column_Name'].value_counts() <-- calcul la fréquence des données d'une colonne
import pandas as pd
import plotly
import numpy as np
#import plotly.plotly as py
import plotly.graph_objs as go
#from collections import Counter
import operator
#from plotly.offline import download_plotlyjs
   
    
def outputContinuous(data,columnName,TypeActivity,fileName):
    #columnName : Tableau de chaînes de caractères qui sont les noms des colonnes
    #fileName : Name of the files generated
    
    res = pd.DataFrame(data.as_matrix(columnName), columns=columnName)
    switchContinuous(res,TypeActivity,fileName)
    reportContinuous(res,TypeActivity,fileName)

def reportContinuous(df,TypeActivity,fileName):
    
    miss = []
    for key in df:
        miss.append(df[key].tolist().count("NaN")/df[key].count()*100)
    df = df.describe().transpose()
    df['miss'] = miss
    df.to_csv('./Data/D-DQR/'+TypeActivity+"/"+fileName+'_continuous.csv')
    
    
def reportCategorical(df,TypeActivity,fileName):
    
    miss = []
    temp = {}
    for key in df:
        
        count = df[key].count()
        miss = df[key].tolist().count("NaN")/df[key].count()*100
        card = df[key].nunique()
        values={}
        for value in df[key]:
            if value in values:
                values[value]+=1
            else:
                values[value]=1
        valuesS = sorted(values.items(), key=operator.itemgetter(1), reverse=True)
        mode = valuesS[0][0]
        modeF = valuesS[0][1]
        modeP = modeF/count*100
        if modeP == 100:
            mode2 = '-'
            modeF2 = '-'
            modeP2 = '-'
        else:
            mode2 = valuesS[1][0]
            modeF2 = valuesS[1][1]
            modeP2 = modeF2/count*100
        temp[key] = [count, miss, card, mode, modeF, modeP, mode2, modeF2, modeP2]
    df = pd.DataFrame(temp, index=["count", "miss", "card", "mode", "modeF", "modeP", "mode2", "modeF2", "modeP2"]).transpose()
    #print(df)
    df.to_csv('./Data/D-DQR/'+TypeActivity+"/"+fileName+'_categorical.csv')
    
def outputCategorical(data,columnName,TypeActivity,fileName):
    res = pd.DataFrame(data.as_matrix(columnName), columns=columnName )
    switchCategorical(res,TypeActivity,fileName)
    reportCategorical(res,TypeActivity,fileName)
 
def getCardinality(data):
    return data.apply(pd.Series.nunique)

def switchContinuous(data,TypeActivity,fileName):
    cardinalities = getCardinality(data)
    for key, cardinality in cardinalities.iteritems():
        if cardinality < 10:
            barPlot(data.as_matrix([key]),key,TypeActivity,fileName)
        else:
            histogram(data.as_matrix([key]),data.index.values,key,TypeActivity,fileName)
        
def switchCategorical(data,TypeActivity,fileName):
    for key in list(data):
        barPlot(data.as_matrix([key]),key,TypeActivity,fileName)
    
def histogram(data,index,key,TypeActivity,fileName):
    plotly.tools.set_credentials_file(username='Steyner', api_key='QweArHhlztVwiP0QUAfg')
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
    array = []
    for value in data:
        array.append(value[0])
        
    trace = go.Histogram(
            x=array,
            name=key)
    
    
    ToPlot = go.Figure(data=[trace],layout=layout)
    
    plotly.offline.plot(ToPlot, filename = './Plots/'+TypeActivity+"/Histogram/"+fileName+'_'+key+'.html')
    
def barPlot(data,name,TypeActivity,fileName):
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
    
    
    plotly.offline.plot(ToPlot, filename = './Plots/'+TypeActivity+"/Bar/"+fileName+'_'+name+'.html')
