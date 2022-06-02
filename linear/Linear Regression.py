#Simple Linear Regression
###########################
#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as mtp

data_set = pd.read_csv("Salary_Data.csv")

#print(data_set)
#split data into dependatn and independant
# -1 to remove the last column (1)  to extract the second colum(1)
x = data_set.iloc[:, :-1]
y = data_set.iloc[:, 1]
#print(x, y)
# Splitting the dataset into training and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/3)
#print(x_test, y_test)
##Fitting the Simple Linear Regression model to the training dataset  
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(x_train, y_train)
print("Intercept", reg.intercept_)
print("coffecient", reg.coef_)

#Prediction of Test and Training set result  
y_pred= reg.predict(x_test)
x_pred= reg.predict(x_train)
###############################################################
df = pd.DataFrame({'Actual': y_test, 'predict': y_pred})
print(df)
###############################################################
#Print Errors
from sklearn import metrics
print("Mean Absolute Error", metrics.mean_absolute_error(y_test, y_pred))
print("Mean Squared Error", metrics.mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))



################################################################
#mtp.scatter(x_train, y_train, color="green")
data_set.plot(x="YearsExperience", y="Salary")
mtp.plot(x_test, y_pred, color="red")    
mtp.title("Salary vs Experience (Training Dataset)")  
mtp.xlabel("Years of Experience")  
mtp.ylabel("Salary")  
mtp.show()  

