####################################
# By calculating the mean:
# In this way, we will calculate the mean of that column or row which contains any missing value and will put it on the place of missing value.
# This strategy is useful for the features which have numeric data such as age, salary, year, etc. Here, we will use this approach.

# To handle missing values,
# we will use Scikit-learn library in our code,
# which contains various libraries for building machine learning models.
# Here we will use Imputer class of sklearn.preprocessing library. Below is the code for it:
###################################
###################################

#handling missing data (Replacing missing data with the mean value)  
from sklearn.preprocessing import Imputer  
imputer= Imputer(missing_values ='NaN', strategy='mean', axis = 0)  
#Fitting imputer object to the independent variables x.   
imputerimputer= imputer.fit(x[:, 1:3])  
#Replacing missing data with the calculated mean value  
x[:, 1:3]= imputer.transform(x[:, 1:3])  
