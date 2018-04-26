# -*- coding: utf-8 -*-
from sklearn.model_selection import cross_val_score
from sklearn import tree
from sklearn.metrics import classification_report, confusion_matrix 
from sklearn.neighbors import KNeighborsClassifier  
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix  
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import pandas as pd
import graphviz as gr
import numpy as np

def main():
    
    data = pd.read_csv("./bill_authentication.csv")
    
    X = data.drop(['Class'], axis=1)  
    y = data['Class']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)  
    
    classifier = KNeighborsClassifier(n_neighbors=5)  
    classifier.fit(X_train, y_train) 
    
    y_pred = classifier.predict(X_test)
    
    print(confusion_matrix(y_test, y_pred))  
    print(classification_report(y_test, y_pred))  
    
    # creating odd list of K for KNN
    myList = list(range(1,50))
    
    # subsetting just the odd ones
    neighbors = filter(lambda x: x % 2 != 0, myList)
    
    # empty list that will hold cv scores
    cv_scores = []
    
    # perform 10-fold cross validation
    for k in neighbors:
        knn = KNeighborsClassifier(n_neighbors=k)
        scores = cross_val_score(knn, X_train, y_train, cv=10, scoring='accuracy')
        cv_scores.append(scores.mean())
        
    # changing to misclassification error
    MSE = [1 - x for x in cv_scores]
    
    # determining best k
    optimal_k = neighbors[MSE.index(min(MSE))]
    print ("The optimal number of neighbors is %d" % optimal_k)
    
    # plot misclassification error vs k
    plt.plot(neighbors, MSE)
    plt.xlabel('Number of Neighbors K')
    plt.ylabel('Misclassification Error')
    plt.show()
    
main()