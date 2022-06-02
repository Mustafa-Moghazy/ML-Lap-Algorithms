{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "b28b6878",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "confusion matrix [[131  64]\n",
      " [ 54  97]]\n",
      " Accurcy 0.6589595375722543\n",
      "precision 0.6024844720496895\n",
      "f1 score 0.6217948717948717\n",
      "recall 0.6423841059602649\n"
     ]
    }
   ],
   "source": [
    "# Import Libries // PreProcessing\n",
    "import pandas as pd\n",
    "\n",
    "data_set = pd.read_csv('data.csv')\n",
    "\n",
    "x = data_set.iloc[:, :-1 ]\n",
    "y = data_set.iloc[:, 19]\n",
    "\n",
    "# Split data into train && test\n",
    "\n",
    "from sklearn.model_selection import train_test_split \n",
    "x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)\n",
    "\n",
    "from sklearn.ensemble import RandomForestClassifier \n",
    "classifier = RandomForestClassifier(n_estimators = 10)\n",
    "\n",
    "classifier.fit(x_train, y_train)\n",
    "\n",
    "y_pred = classifier.predict(x_test)\n",
    "\n",
    "from sklearn.metrics import confusion_matrix \n",
    "conf = confusion_matrix(y_pred, y_test)\n",
    "\n",
    "from sklearn import metrics \n",
    "print('confusion matrix', conf) \n",
    "print(' Accurcy', metrics.accuracy_score(y_pred,y_test)) \n",
    "print('precision', metrics.precision_score(y_pred,y_test)) \n",
    "print('f1 score', metrics.f1_score(y_pred,y_test)) \n",
    "print('recall', metrics.recall_score(y_pred,y_test))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d951ead4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
