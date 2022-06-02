{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2f2bcafa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[9.99989746e-01 6.21988689e-06 3.98396312e-06 3.76304943e-08\n",
      " 8.43631768e-09]\n"
     ]
    },
    {
     "data": {
      "image/png": "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qYcov/XWW/nWt75F165dT/jz4jqf+owxk5QIRE5SI0eOrKw5lMr999+fpmjS72Qv4dyQykzXRE1DImmwYsUKhgwZwqhRo+jSpQvXX399Zenj3/3ud3Tp0oVBgwYdU+1yzpw5TJ06lf3795OXl1dZW+jw4cN06NCBTz75pLIyaXXHmTFjRmVFS4Du3buzfft2IHU55VRUZrphlpmuiRKBSJq88sorPPLII5SWlvLmm2+yevVqPvroI2677TYWLVrEH/7wB957773j9jvjjDPo2bMnK1euBGDRokVccsklNG3atHKbKMdJJlU55WRUZrrhlpmuiRKBSJr079+f9u3b06RJE3r16sX27dvZsmULnTp1onPnzpgZ48ePT7rvmDFjKscJmDdvXuUvrApRj1NVYWFh5V/ZFeWUU0ksM92rVy+eeOIJ3n77bSBoKz948CBFRUXHXH1ULTP9xz/+8bjjzp8/nz59+tC7d282bdqUdGjHqmWmK65oli1bxtSpU+nVqxcjR448psx0xXcQpcz03r17jysznex7qanMdKrzSCwznRj7lClTKrdp2bJltd9xnHSPQCRNEstJJ5YbjlIOeeTIkdx999188MEHrFu3jmHDhh23TarjpCpZXV055WRUZrrhlpmuia4IRDKoS5cuvPXWW/zP//wPQMpfAM2bN6d///7ceeedXHHFFcf9MqruOHl5eaxfvx6A9evX89ZbbwG1L6esMtOpnexlpmuiKwLJGidjxdbc3FxmzZrF5ZdfTuvWrRk0aFDK+jtjxoxh9OjRrFixolbHueaaa3jyySfp1asX/fr149xzzwWCcspFRUXk5+dz3nnn1VhOObEE8pEjRwB48MEH2blzJ8XFxaxevZqcnBwWLlzI448/ztChQyvLTE+cOJHOnTtXW2b67LPPrlOZ6SlTppCfn095eTmDBw+mqKiI6dOnM27cOPr06cPFF19cY5np0tLSY8pM1+Z7qet53HPPPUyZMoXu3buTk5PD9OnTufrqq5N+xxX/ZnFRGeoG6mT8pXayURnqzFKZ6cxRGWoREakVJQIRiYXKTDccSgTSqDW0pk+RE1WXn3klAmm0cnNz2bt3r5KBZA13Z+/eveTm5tZqP/Uakkarffv2lJWVsXv37kyHIpI2ubm5tG/fvlb7KBFIo9W0aVM6deqU6TBETnqxNg2Z2Qgz22pm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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.decomposition import PCA\n",
    "from sklearn import metrics \n",
    "\n",
    "df = pd.read_csv('cleaned_gender.csv')  \n",
    "X = df.drop('label', axis=1)\n",
    "y = df['label']\n",
    "\n",
    "pca = PCA(n_components=5)\n",
    "\n",
    "pc = pca.fit_transform(X)\n",
    "\n",
    "pDf = pd.DataFrame( data = pc, columns = ['A', 'B', 'C', 'D', 'E'])\n",
    "\n",
    "finalDf = pd.concat([pDf, y], axis = 1)\n",
    "\n",
    "finalDf.to_csv(\"pcadata.csv\", index=False, header=True)  \n",
    "\n",
    "\n",
    "exvar = pca.explained_variance_ratio_\n",
    "cexvarsum = np.cumsum(exvar)\n",
    "print(\"cumulative sum\", exvar)\n",
    "\n",
    "plt.bar(range(0, len(exvar)), exvar, label='Individual explained variance')  # نسبة تأثير كل attribute\n",
    "\n",
    "plt.step(range(0, len(cexvarsum)), cexvarsum, label='Cumulative explained variance')   #نسبة تأثير كله\n",
    "\n",
    "plt.ylabel('Explained variance ratio')\n",
    "plt.xlabel('Principal component index')\n",
    "\n",
    "plt.legend(loc='lower right')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "483f888e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[152 154]\n",
      " [102 901]]\n",
      "accuracy  0.8044308632543926\n",
      "recall 0.8044308632543926\n",
      "f1_score 0.8044308632543926\n",
      "precision_score 0.8044308632543926\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.metrics import confusion_matrix\n",
    "from sklearn.metrics import accuracy_score\n",
    "from sklearn.metrics import f1_score\n",
    "from sklearn.metrics import recall_score\n",
    "from sklearn.metrics import precision_score\n",
    "\n",
    "data = pd.read_csv('pcadata.csv')\n",
    "X = data.drop('label', axis=1)\n",
    "y = data['label']\n",
    "\n",
    "x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)\n",
    "\n",
    "rf = RandomForestClassifier(n_estimators=10)\n",
    "rf.fit(x_train, y_train)\n",
    "\n",
    "predictions = rf.predict(x_test)\n",
    "matrix = confusion_matrix(y_test, predictions)\n",
    "print(matrix)\n",
    "acc = accuracy_score(y_test, predictions)\n",
    "print(\"accuracy \", acc)\n",
    "print('recall', recall_score(predictions , y_test , average='micro'))\n",
    "print('f1_score', f1_score(predictions , y_test , average='micro'))\n",
    "print('precision_score', precision_score(predictions , y_test , average='micro'))"
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
