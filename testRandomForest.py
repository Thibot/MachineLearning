# -*- coding: utf-8 -*-

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
import pandas as pd

def main():
    
    data = pd.read_csv("./bill_authentication.csv")

    X = data.drop(['Class'], axis=1)   
    y = data['Class'] 
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    
    clf = RandomForestClassifier(max_depth=2, random_state=0)
    
    clf.fit(X_train, y_train)
    
    y_pred = clf.predict(X_test)
    
    print("Confusion matrix : \n", confusion_matrix(y_test, y_pred))   
    print("Classification report : \n", classification_report(y_test, y_pred))
    print("Accuracy score : \n", accuracy_score(y_test, y_pred))
    print("Cross validation score : \n", cross_val_score(clf, X, y, cv = 5))
    
main()# -*- coding: utf-8 -*-