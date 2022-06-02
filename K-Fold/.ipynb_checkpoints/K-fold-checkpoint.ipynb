{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "08846baa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "accuracy 0.6689591567852438\n",
      "precision_score =  0.6822429906542056\n",
      "f1 =  0.6547085201793722\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "data=pd.read_csv('diabetics.csv')\n",
    "# data.shape\n",
    "# data.head()\n",
    "x=data.drop('outcome',axis=1)\n",
    "y=data['outcome']\n",
    "\n",
    "from sklearn.model_selection import KFold\n",
    "k = 5\n",
    "kfold = KFold(n_splits = k, random_state = None, shuffle=False)\n",
    "acclist=[]\n",
    "\n",
    "\n",
    "for train_index, test_index in kfold.split(x):\n",
    "    #print(train_index)\n",
    "    x_train, x_test = x.iloc[train_index, : ], x.iloc[test_index, : ]\n",
    "    #print(x_train)\n",
    "    y_train, y_test = y[train_index], y[test_index]\n",
    "    \n",
    "    from sklearn.ensemble import RandomForestClassifier\n",
    "    rf = RandomForestClassifier(n_estimators=10)\n",
    "    rf.fit(x_train, y_train)\n",
    "    predictions = rf.predict(x_test)\n",
    "    \n",
    "    from sklearn.metrics import accuracy_score\n",
    "    acc = accuracy_score(y_test, predictions)\n",
    "    #print(\"acc = \", acc)\n",
    "    acclist.append(acc)\n",
    "    \n",
    "\n",
    "acc=sum(acclist)/k\n",
    "print(\"accuracy\", acc)\n",
    "\n",
    "from sklearn.metrics import precision_score\n",
    "precision=precision_score(y_test,predictions)\n",
    "print(\"precision_score = \", precision)\n",
    "\n",
    "from sklearn.metrics import f1_score\n",
    "f1 = f1_score(y_test, predictions)\n",
    "print(\"f1 = \", f1)\n"
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
