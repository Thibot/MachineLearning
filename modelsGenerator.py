# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 22:55:19 2018

@author: Bastien
"""
from sklearn import tree
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix  
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets

import pandas as pd
import graphviz as gr

#make the model of the dataset with the random forest technique
def randomForest(data, target, cv):
    X = data.drop([target], axis=1)   
    y = data[target] 
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    
    clf = RandomForestClassifier(max_depth=2, random_state=0)
    
    clf.fit(X_train, y_train)
    
    y_pred = clf.predict(X_test)
    
    print("Confusion matrix : \n", confusion_matrix(y_test, y_pred))   
    print("Classification report : \n", classification_report(y_test, y_pred))
    if (cv != 0):
        print("Accuracy score : \n", accuracy_score(y_test, y_pred))
        print("Cross validation score : \n", cross_val_score(clf, X, y, cv = cv))
    
    return clf

#make the model of the dataset with the random forest technique and entropy gestion
def randomForestWithEntropy(data, target, cv):
    X = data.drop([target], axis=1)   
    y = data[target] 
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    
    clf = RandomForestClassifier(max_depth=2, random_state=0, criterion = "entropy")
    
    clf.fit(X_train, y_train)
    
    y_pred = clf.predict(X_test)
    
    print("Confusion matrix : \n", confusion_matrix(y_test, y_pred))   
    print("Classification report : \n", classification_report(y_test, y_pred))
    if (cv != 0):
        print("Accuracy score : \n", accuracy_score(y_test, y_pred))
        print("Cross validation score : \n", cross_val_score(clf, X, y, cv = cv))
    
    return clf

#make the model of the dataset with the decison tree technique
def decisionTree(data, target, cv):
    X = data.drop([target], axis=1)  
    y = data[target]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.50
    )
    
    clf = tree.DecisionTreeClassifier()
    clf.fit(X=X_train, y=y_train)
    y_pred = clf.predict(X_test)

    print("Confusion matrix : \n", confusion_matrix(y_test, y_pred))    
    print("Classification report : \n", classification_report(y_test, y_pred))
    if (cv != 0):
        print("Accuracy score : \n", accuracy_score(y_test, y_pred))
        print("Cross validation score : \n", cross_val_score(clf, X, y, cv = cv))

    #decision_tree = tree.export_graphviz(clf, out_file=None) 
    #graph = gr.Source(decision_tree) 
    #graph.render("decision_tree")
    
    return clf

#make the model of the dataset with the decison tree technique and entropy gestion
def decisionTreeWithEntropy(data, target, cv):
    
    X = data.drop([target], axis=1)  
    y = data[target]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.50
    )
    
    clf = tree.DecisionTreeClassifier(criterion = "entropy")
    clf.fit(X=X_train, y=y_train)
    y_pred = clf.predict(X_test)

    print("Confusion matrix : \n", confusion_matrix(y_test, y_pred))    
    print("Classification report : \n", classification_report(y_test, y_pred)) 
    if (cv != 0):
        print("Accuracy score : \n", accuracy_score(y_test, y_pred))
        print("Cross validation score : \n", cross_val_score(clf, X, y, cv = cv))

    #decision_tree = tree.export_graphviz(clf, out_file=None) 
    #graph = gr.Source(decision_tree) 
    #graph.render("decision_tree_entropy")
    
    return clf
    
#make the model of the dataset with the decison nearest neighbors technique
def nearestNeighbors(data, target, cv):

    X = data.drop([target], axis=1)  
    y = data[target]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.50)  
    
    clf = KNeighborsClassifier(n_neighbors=5)  
    clf.fit(X_train, y_train) 
    
    y_pred = clf.predict(X_test)    

    print("Confusion matrix : \n", confusion_matrix(y_test, y_pred))   
    print("Classification report : \n", classification_report(y_test, y_pred))
    if (cv != 0):
        print("Accuracy score : \n", accuracy_score(y_test, y_pred))
        print("Cross validation score : \n", cross_val_score(clf, X, y, cv = cv))
    
    return clf
