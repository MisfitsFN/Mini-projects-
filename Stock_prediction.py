#This code uses AI to predict the stock Prices of Ford 
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
ticker= yf.Ticker('F')
dataset_train =ticker.history(start='2015-1-10',end='2023-4-30')
training_set = dataset_train.iloc[:, 1:2].values  

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range=(0,1))
training_set_scaled = sc.fit_transform(training_set) 

X_train = []
y_train = []
for i in range(60, 2035):
    X_train.append(training_set_scaled[i-60:i, 0])
    y_train.append(training_set_scaled[i, 0])
X_train, y_train = np.array(X_train), np.array(y_train)

X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dropout
from keras.layers import Dense 

model = Sequential()

model.add(LSTM(units=50,return_sequences=True,input_shape=(X_train.shape[1], 1)))
model.add(Dropout(0.2))

model.add(LSTM(units=50,return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(units=50,return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(units=50))
model.add(Dropout(0.2))

model.add(Dense(units=1))

model.compile(optimizer='adam',loss='mean_squared_error')

model.fit(X_train,y_train,epochs=100,batch_size=32) 

dataset_test =ticker.history(start='2023-5-1',end='2023-5-22')
real_stock_price = dataset_test.iloc[:, 1:2].values 

dataset_total = pd.concat((dataset_train['Open'], dataset_test['Open']), axis = 0)
inputs = dataset_total[len(dataset_total) - len(dataset_test) - 60:].values
inputs = inputs.reshape(-1,1)
inputs = sc.transform(inputs)


X_test = []
for i in range(60, 76):
    X_test.append(inputs[i-60:i, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
X_test=X_test
predicted_stock_price = model.predict(X_test)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)
predicted_stock_price=predicted_stock_price 

plt.plot(real_stock_price, color = 'black', label = 'Ford stock prices ($)')
plt.plot(predicted_stock_price, color = 'green', label = 'Predicted stock prices of Ford ($)')
plt.title('Predicted stock prices of Ford ($)')
plt.xlabel('Time (Days)')
plt.ylabel('Ford stock prices ($)')
plt.legend()
plt.show()
