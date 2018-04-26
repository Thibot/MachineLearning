# -*- coding: utf-8 -*-

from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix  
import pandas as pd
import graphviz as gr
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

def main():
    
    data = pd.read_csv("./bill_authentication.csv")
    
    data['is_train'] = np.random.uniform(0, 1, len(data)) <= .75
    
    train, test = data[data['is_train']==True], data[data['is_train']==False]
    
    features = data.columns[:4]
    
    clf = RandomForestClassifier(max_depth=2, random_state=0)
    
    y = train['Class']
    y_test = train[features]
    clf.fit(y_test, y)
    
    y_pred = clf.predict(test[features])

    print(confusion_matrix(y_test, y_pred))  
    print(classification_report(y_test, y_pred))
    
main()# -*- coding: utf-8 -*-

