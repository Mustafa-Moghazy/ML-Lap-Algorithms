import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn import metrics 

df = pd.read_csv('cleaned_gender.csv')  
X = df.drop('label', axis=1)
y = df['label']

pca = PCA(n_components=5)

pc = pca.fit_transform(X)

pDf = pd.DataFrame( data = pc, columns = ['A', 'B', 'C', 'D', 'E'])

finalDf = pd.concat([pDf, y], axis = 1)

finalDf.to_csv("pcadata.csv", index=False, header=True)  


exvar = pca.explained_variance_ratio_
cexvarsum = np.cumsum(exvar)
print("cumulative sum", exvar)

plt.bar(range(0, len(exvar)), exvar, label='Individual explained variance')  # نسبة تأثير كل attribute

plt.step(range(0, len(cexvarsum)), cexvarsum, label='Cumulative explained variance')   #نسبة تأثير كله

plt.ylabel('Explained variance ratio')
plt.xlabel('Principal component index')

plt.legend(loc='lower right')

plt.show()
#####################################################################################################################
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score

data = pd.read_csv('pcadata.csv')
X = data.drop('label', axis=1)
y = data['label']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

rf = RandomForestClassifier(n_estimators=10)
rf.fit(x_train, y_train)

predictions = rf.predict(x_test)
matrix = confusion_matrix(y_test, predictions)
print(matrix)
acc = accuracy_score(y_test, predictions)
print("accuracy ", acc)
print('recall', recall_score(predictions , y_test , average='micro'))
print('f1_score', f1_score(predictions , y_test , average='micro'))
print('precision_score', precision_score(predictions , y_test , average='micro'))
