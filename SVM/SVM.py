{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "513904b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[   0  408]\n",
      " [   0 1337]]\n",
      " Accurcy 0.766189111747851\n",
      "recall 0.766189111747851\n",
      "f1_score 0.766189111747851\n",
      "precision_score 0.766189111747851\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn import svm\n",
    "from sklearn import metrics \n",
    "from sklearn.ensemble import RandomForestClassifier \n",
    "from sklearn.metrics import confusion_matrix \n",
    "from sklearn.metrics import recall_score\n",
    "from sklearn.metrics import f1_score\n",
    "from sklearn.metrics import precision_score\n",
    "data = pd.read_csv('pcadata.csv')\n",
    "\n",
    "x= data.drop('label', axis=1)\n",
    "y=data['label']\n",
    " \n",
    "x_train, x_test, y_tarin, y_test = train_test_split(x,y,test_size=0.4)\n",
    "\n",
    "classifier = svm.SVC(kernel='rbf')\n",
    "classifier.fit(x_train, y_tarin)\n",
    "\n",
    "prediction = classifier.predict(x_test)\n",
    "\n",
    "cm = confusion_matrix(y_test, prediction)\n",
    "print(cm)\n",
    "\n",
    "print(' Accurcy',metrics.accuracy_score(prediction,y_test))\n",
    "print('recall', recall_score(prediction , y_test , average='micro'))\n",
    "print('f1_score', f1_score(prediction , y_test , average='micro'))\n",
    "print('precision_score', precision_score(prediction , y_test , average='micro'))"
   ]
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
