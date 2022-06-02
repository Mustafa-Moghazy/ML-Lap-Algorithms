import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
data = pd.read_csv('pcadata.csv')

x= data.drop('label', axis=1)
y=data['label']
 
x_train, x_test, y_tarin, y_test = train_test_split(x,y,test_size=0.4)

classifier = svm.SVC(kernel='rbf')
classifier.fit(x_train, y_tarin)

prediction = classifier.predict(x_test)

cm = confusion_matrix(y_test, prediction)
print(cm)

print(' Accurcy',metrics.accuracy_score(prediction,y_test))
print('recall', recall_score(prediction , y_test , average='micro'))
print('f1_score', f1_score(prediction , y_test , average='micro'))
print('precision_score', precision_score(prediction , y_test , average='micro'))
