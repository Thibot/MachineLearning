# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 22:55:19 2018

@author: Bastien
"""
from sklearn import tree
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

# LIBRARY FOR GENERATE THE TREE VISUALISATION
# import graphviz as gr

#make the model of the dataset with the random forest technique
def randomForest(data, target, cv):
    # getting array of imput values
    X = data.drop([target], axis=1)   
    # getting array of target values 
    y = data[target] 
    
    # getting training array and test array
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    
    # initialise the random forest model
    clf = RandomForestClassifier(max_depth=2, random_state=0)
    
    # generate model with training array
    clf.fit(X_train, y_train)
    
    # predict target from test array
    y_pred = clf.predict(X_test)
    
    if (cv != 0): 
        print("Confusion matrix : \n", confusion_matrix(y_test, y_pred))   
        print("Classification report : \n", classification_report(y_test, y_pred))
        print("Accuracy score : \n", accuracy_score(y_test, y_pred))
        print("Cross validation score : \n", cross_val_score(clf, X_test, y_test, cv = cv))
    
    return clf

#make the model of the dataset with the random forest technique and entropy gestion
def randomForestWithEntropy(data, target, cv):
    # getting array of imput values
    X = data.drop([target], axis=1)  
    # getting array of target values 
    y = data[target] 
    
    # getting training array and test array
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    
    # initialise the random forest model with entropy
    clf = RandomForestClassifier(max_depth=2, random_state=0, criterion = "entropy")
    
    # generate model with training array
    clf.fit(X_train, y_train)
    
    # predict target from test array
    y_pred = clf.predict(X_test)
    
    if (cv != 0):
        print("Confusion matrix : \n", confusion_matrix(y_test, y_pred))   
        print("Classification report : \n", classification_report(y_test, y_pred))
        print("Accuracy score : \n", accuracy_score(y_test, y_pred))
        print("Cross validation score : \n", cross_val_score(clf, X_test, y_test, cv = cv))
    
    return clf

#make the model of the dataset with the decison tree technique
def decisionTree(data, target, cv):
    # getting array of imput values
    X = data.drop([target], axis=1)  
    # getting array of target values 
    y = data[target]
    
    # getting training array and test array with a training size of 0.5
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.50
    )
    
    # initialise the decision tree model
    clf = tree.DecisionTreeClassifier()
    
    # generate model with training array
    clf.fit(X=X_train, y=y_train)
    
    # predict target from test array
    y_pred = clf.predict(X_test)

    if (cv != 0):
        print("Confusion matrix : \n", confusion_matrix(y_test, y_pred))    
        print("Classification report : \n", classification_report(y_test, y_pred))
        print("Accuracy score : \n", accuracy_score(y_test, y_pred))
        print("Cross validation score : \n", cross_val_score(clf, X_test, y_test, cv = cv))

    # -- GENERATE A PDF FOR THE CREATED DECISION TREE --
    #decision_tree = tree.export_graphviz(clf, out_file=None) 
    #graph = gr.Source(decision_tree) 
    #graph.render("decision_tree")
    
    return clf

#make the model of the dataset with the decison tree technique and entropy gestion
def decisionTreeWithEntropy(data, target, cv):
    # getting array of imput values
    X = data.drop([target], axis=1)
    # getting array of target values 
    y = data[target]
    
    # getting training array and test array with a training size of 0.5
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.50
    )
    
    # initialise the decision tree model with entropy
    clf = tree.DecisionTreeClassifier(criterion = "entropy")
    
    # generate model with training array
    clf.fit(X=X_train, y=y_train)
    
    # predict target from test array
    y_pred = clf.predict(X_test)

    if (cv != 0):
        print("Confusion matrix : \n", confusion_matrix(y_test, y_pred))    
        print("Classification report : \n", classification_report(y_test, y_pred)) 
        print("Accuracy score : \n", accuracy_score(y_test, y_pred))
        print("Cross validation score : \n", cross_val_score(clf, X_test, y_test, cv = cv))

    # -- GENERATE A PDF FOR THE CREATED DECISION TREE --
    #decision_tree = tree.export_graphviz(clf, out_file=None) 
    #graph = gr.Source(decision_tree) 
    #graph.render("decision_tree_entropy")
    
    return clf
    
#make the model of the dataset with the decison nearest neighbors technique
def nearestNeighbors(data, target, cv):
    # getting array of imput values
    X = data.drop([target], axis=1)
    # getting array of target values 
    y = data[target]
    
    # getting training array and test array with a training size of 0.5
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.50)  
    
    # initialise the k-nearest neighbors model
    clf = KNeighborsClassifier(n_neighbors=5)
    
    # generate model with training array
    clf.fit(X_train, y_train) 
    
    # predict target from test array
    y_pred = clf.predict(X_test)    
    if (cv != 0):
        print("Confusion matrix : \n", confusion_matrix(y_test, y_pred))   
        print("Classification report : \n", classification_report(y_test, y_pred))
        print("Accuracy score : \n", accuracy_score(y_test, y_pred))
        print("Cross validation score : \n", cross_val_score(clf, X_test, y_test, cv = cv))
    
    return clf
