# -*- coding: utf-8 -*-
"""Basic_python_Implementation_for_Neural_Nets.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iz99X7DDQDFCyIGVx7gQUFzZt35znGze
"""

import pandas as pd
import numpy as np

data=pd.read_csv('/content/drive/MyDrive/AIE/Churn_Modelling.csv')

# Business problem: - To find out whether cutomers will leave the same or not

from google.colab import drive
drive.mount('/content/drive')

data.head()

data.tail()

## Missing value check
data.isnull().sum()

# conversion of categorical data
Geography = pd.get_dummies(data['Geography'],drop_first=True)
Gender = pd.get_dummies(data['Gender'],drop_first=True)

data=pd.concat([data,Geography,Gender],axis=1)

data.drop(['Geography','Gender'],axis=1,inplace=True)

data.columns

Geography

## Creating independent and dependent variable.
X=data.loc[:,['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
       'IsActiveMember', 'EstimatedSalary', 'Germany', 'Spain',
       'Male']]
y=data.loc[:,['Exited']]

y

# Training and tetsing data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=20)

X_train.shape

X_test.shape

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LeakyReLU,PReLU,ELU,ReLU
from tensorflow.keras.layers import Dropout

# Define the model
model=Sequential()

# Adding input layer to first hidden layer
model.add(Dense(units=11,input_dim=11,activation='relu',
                kernel_initializer='he_uniform')) # Fixed typo here


# Adding first hidden layer to second hidden layer
model.add(Dense(units=16,activation='relu',kernel_initializer='he_uniform')) # Fixed typo: kernal_initializer -> kernel_initializer

# Adding second hidden layer to output layer
model.add(Dense(units=8,activation='relu',kernel_initializer='he_uniform'))

# Adding third hidden layer to output layer
model.add(Dense(units=1,activation='sigmoid',kernel_initializer='glorot_uniform'))

model.summary()

X_train.shape

# fit the keras model on the dataset
model_history=model.fit(X_train,y_train,validation_split=0.33,batch_size=10,epochs=100)

...
# Compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam',
              metrics=['accuracy'])

...
# evaluate the keras model
accuracy = model.evaluate(X_test, y_test)
accuracy

# list all data in history
print(model_history.history.keys())

model_history.history

# summarize history for accuracy
import matplotlib.pyplot as plt
plt.plot(model_history.history['accuracy'])
plt.plot(model_history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# summarize history for loss
import matplotlib.pyplot as plt
plt.plot(model_history.history['loss'])
plt.plot(model_history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# Making the predictions and evaluating the model

# Predicting the Test set results
y_pred = model.predict(X_test)
y_pred = (y_pred > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
cm

# Calculating the Accuracy
from sklearn.metrics import accuracy_score
score=accuracy_score(y_pred,y_test)
score

