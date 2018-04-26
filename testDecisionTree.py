# -*- coding: utf-8 -*-

from sklearn import tree
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix  
import pandas as pd
import graphviz as gr

def main():
    
    data = pd.read_csv("./bill_authentication.csv")
    
    X = data.drop(['Class'], axis=1)  
    y = data['Class']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20
    )
    
    clf = tree.DecisionTreeClassifier()
    clf.fit(X=X_train, y=y_train)
    y_pred = clf.predict(X_test)

    print("Confusion matrix : \n", confusion_matrix(y_test, y_pred))    
    print("Classification report : \n", classification_report(y_test, y_pred))
    print("Accuracy score : \n", accuracy_score(y_test, y_pred)) 
    print("Cross validation score : \n", cross_val_score(clf, X, y, cv = 5))

    decision_tree = tree.export_graphviz(clf, out_file=None) 
    graph = gr.Source(decision_tree) 
    graph.render("decision_tree")
    
    data = pd.read_csv("./bill_authentication.csv")
    
    X = data.drop(['Class'], axis=1)  
    y = data['Class']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20
    )
    
    clf = tree.DecisionTreeClassifier(criterion = "entropy")
    clf.fit(X=X_train, y=y_train)
    y_pred = clf.predict(X_test)

    print("Confusion matrix : \n", confusion_matrix(y_test, y_pred))    
    print("Classification report : \n", classification_report(y_test, y_pred)) 
    print("Accuracy score : \n", accuracy_score(y_test, y_pred)) 
    print("Cross validation score : \n", cross_val_score(clf, X, y, cv = 5)) 

    decision_tree = tree.export_graphviz(clf, out_file=None) 
    graph = gr.Source(decision_tree) 
    graph.render("decision_tree_entropy")
main()