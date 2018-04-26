# -*- coding: utf-8 -*-
from sklearn.model_selection import cross_validate
from sklearn.metrics import classification_report, confusion_matrix 
from sklearn.neighbors import KNeighborsClassifier  
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn import metrics
import pandas as pd

def main():
    
    data = pd.read_csv("./bill_authentication.csv")
    
    X = data.drop(['Class'], axis=1)  
    y = data['Class']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)  
    
    classifier = KNeighborsClassifier(n_neighbors=5)  
    classifier.fit(X_train, y_train) 
    
    y_pred = classifier.predict(X_test)
    
    #print(confusion_matrix(y_test, y_pred))  
    #print(classification_report(y_test, y_pred))  
    
    print(accuracy_score(y_test, y_pred))
    
    scores =  cross_val_score(classifier, X_train, y_train, cv = 5)
    print((scores))
    
    #predicted =  cross_val_predict(classifier, X, y, cv = 20)
    #print(metrics.accuracy_score(y, predicted))
    
main()