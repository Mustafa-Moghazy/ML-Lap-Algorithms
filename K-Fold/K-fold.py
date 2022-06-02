import pandas as pd
data=pd.read_csv('diabetics.csv')
# data.shape
# data.head()
x=data.drop('outcome',axis=1)
y=data['outcome']

from sklearn.model_selection import KFold
k = 5
kfold = KFold(n_splits = k, random_state = None, shuffle=False)
acclist=[]


for train_index, test_index in kfold.split(x):
    #print(train_index)
    x_train, x_test = x.iloc[train_index, : ], x.iloc[test_index, : ]
    #print(x_train)
    y_train, y_test = y[train_index], y[test_index]
    
    from sklearn.ensemble import RandomForestClassifier
    rf = RandomForestClassifier(n_estimators=10)
    rf.fit(x_train, y_train)
    predictions = rf.predict(x_test)
    
    from sklearn.metrics import accuracy_score
    acc = accuracy_score(y_test, predictions)
    #print("acc = ", acc)
    acclist.append(acc)
    

acc=sum(acclist)/k
print("accuracy", acc)

from sklearn.metrics import precision_score
precision=precision_score(y_test,predictions)
print("precision_score = ", precision)

from sklearn.metrics import f1_score
f1 = f1_score(y_test, predictions)
print("f1 = ", f1)
