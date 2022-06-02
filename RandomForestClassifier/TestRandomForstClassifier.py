# Import Libries // PreProcessing
import pandas as pd

data_set = pd.read_csv('data.csv')

x = data_set.iloc[:, :-1 ]
y = data_set.iloc[:, 19]

# Split data into train && test

from sklearn.model_selection import train_test_split 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)

from sklearn.ensemble import RandomForestClassifier 
classifier = RandomForestClassifier(n_estimators = 10)

classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

from sklearn.metrics import confusion_matrix 
conf = confusion_matrix(y_pred, y_test)

from sklearn import metrics 
print('confusion matrix', conf) 
print(' Accurcy', metrics.accuracy_score(y_pred,y_test)) 
print('precision', metrics.precision_score(y_pred,y_test)) 
print('f1 score', metrics.f1_score(y_pred,y_test)) 
print('recall', metrics.recall_score(y_pred,y_test))
