# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 09:37:34 2018

@author: AKMH
"""
#import libraries
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from datetime import datetime

#Get initial time in milliseconds
start=(datetime.now().minute*60*1000+datetime.now().second*1000+datetime.now().microsecond*0.001)
#Read data from csv file
dataset = pd.read_csv('voicedataset.csv')
# Y is 'label' and X is all data except Y
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
#split train and test data at ratio of 4:1
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
#call decision tree classifier and train data
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)
#predict using that classifier
y_pred = classifier.predict(X_test)
#Get final time in milliseconds
end = datetime.now().minute*60*1000+datetime.now().second*1000+datetime.now().microsecond*0.001
#Display report,accuracy and execution time
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print('Accuracy-DecisionTree : ',accuracy_score(y_pred,y_test))
print("Execution time: %.2f ms" % (abs(end-start)))