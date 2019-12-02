# Simple Linear Regression

'''
This model predicts the salary of the employ based on experience using simple linear regression model.
'''

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import requests
import json
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

# Importing the dataset
df_nilai = pd.read_csv('nilai_sample.csv', sep=';')
df_nilai

# Feature DF for train
feature_df = df_nilai[['mtk', 'bahasa_indo', 'pendidikan_agama', 'ipa', 'ips']]
X = np.asarray(feature_df)
X = preprocessing.StandardScaler().fit(X).transform(X)

# label_encoder object knows how to understand word labels. 
label_encoder = preprocessing.LabelEncoder() 

# Encode labels in column 'species'. 
df_nilai['pernyataan']= label_encoder.fit_transform(df_nilai['pernyataan'])
y = np.asanyarray(df_nilai['pernyataan'])

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=7)

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
LR = LogisticRegression(C=0.01, solver='liblinear').fit(X_train,y_train)

# Predicting the Test set results
yhat = LR.predict(X_test)

# Saving model using pickle
pickle.dump(LR, open('tes_model.pkl','wb'))

# Loading model to compare the results
model = pickle.load( open('tes_model.pkl','rb'))
print(model.predict([[70,80,90,100,77]]))
