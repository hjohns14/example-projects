#Non-Jupyter Version for easy reading and running
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import sklearn.preprocessing as skl
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, TimeDistributed, Flatten
from tensorflow.keras.optimizers import RMSprop
#from keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
from keras import metrics
# import data file here

df = pd.read_excel('data/z_Masterfile.xlsx').dropna()
df[['WTI_Change_PCT', 'WTI_HL_PCT', 'Brent_change_PCT', 'Brent_HL_PCT']] = df[['WTI_Change_PCT', 'WTI_HL_PCT', 'Brent_change_PCT', 'Brent_HL_PCT']]*100
features_considered = ["WTI_price", "WTI_open", "WTI_Change_PCT", "WTI_HL_PCT",
                       "Brent_Price", "Brent_Open", "Brent_change_PCT", "Brent_HL_PCT"]
features = df[features_considered]
features.index = df["Date"]

#Plot Data
features.plot(subplots=True)
time_steps = df.index.size
TRAIN_SPLIT = int(np.rint(time_steps * 0.8))
dataset = features.values
### LOSS CANT BE CALCULATED
print(dataset.shape)
print("Trained Data Points:", TRAIN_SPLIT)
print("Test Data Points: ", time_steps-TRAIN_SPLIT)
#features[["WTI_price", "Brent_Price"]].plot(subplots=True)

# Not Currently used
data_mean = dataset[:TRAIN_SPLIT].mean(axis=0)
data_std = dataset[:TRAIN_SPLIT].std(axis=0)
#Change % mean and std
print(data_mean, data_std)

### FUNCTIONS
#Creates a dataset with a targer range
def multivariate_data(dataset, target, start_index, end_index, history_size,
                      target_size, step, single_step=False):
  data = []
  labels = []

  start_index = start_index + history_size
  if end_index is None:
    end_index = len(dataset) - target_size

  for i in range(start_index, end_index):
    indices = range(i-history_size, i, step)
    data.append(dataset[indices])

    if single_step:
      labels.append(target[i+target_size])
    else:
      labels.append(target[i:i+target_size])

  return np.array(data), np.array(labels)

# Creates a plot of the multivartiate data
def multi_step_plot(history, true_future, prediction, target, path=None, name=None):
  plt.figure(figsize=(12, 6))
  num_in = create_time_steps(len(history))
  num_out = len(true_future)

  plt.plot(num_in, np.array(history[:, target]), label='History')
  plt.plot(np.arange(num_out)/STEP, np.array(true_future), 'bo',
           label='True Future')
  if prediction.any():
    plt.plot(np.arange(num_out)/STEP, np.array(prediction), 'ro',
             label='Predicted Future')
  plt.legend(loc='upper left')
  if path is  not None:
    plt.savefig(path + name)
  plt.show()

#Not Currently used but may be useful
def create_time_steps(length):
  return list(range(-length, 0))

#Plots the training validation and history for each epoch and saves it to a path  and filename
def plot_train_history(history, title, path=None, name=None):
  loss = history.history['loss']
  val_loss = history.history['val_loss']

  epochs = range(len(loss))

  plt.figure()

  plt.plot(epochs, loss, 'b', label='Training loss')
  plt.plot(epochs, val_loss, 'r', label='Validation loss')
  plt.title(title)
  plt.legend()
  if path is  not None:
    plt.savefig(path + name)

  plt.show()


## VARIABLES
past_history = 24
future_target = 12
STEP = 1
BUFFER_SIZE = 25
BATCH_SIZE = 40


# Creating the multivariate datasets
x_train_multi, y_train_multi = multivariate_data(dataset, dataset[:, 2], 0,
                                                   TRAIN_SPLIT, past_history,
                                                   future_target, STEP)
x_val_multi, y_val_multi = multivariate_data(dataset, dataset[:, 2],
                                               TRAIN_SPLIT, None, past_history,
                                               future_target, STEP)

# Looking good
#print("y_train: ", y_train_single.shape, "\ny_val: ", y_val_single.shape)
#print("y_train: ", y_train_single, "\ny_val: ", y_val_single)

train_data_multi = tf.data.Dataset.from_tensor_slices((x_train_multi, y_train_multi))
train_data_multi = train_data_multi.cache().shuffle(BUFFER_SIZE).batch(BATCH_SIZE).repeat()

val_data_multi = tf.data.Dataset.from_tensor_slices((x_val_multi, y_val_multi))
val_data_multi = val_data_multi.batch(BATCH_SIZE).repeat()



'''# Need more data
for x, y in train_data_multi.take(2):
  multi_step_plot(x[0], y[0], np.array([0]), 2)
'''
print("Data Shape: ",x_train_multi.shape[-2:])

# VARIABLES
EPOCHS = 15
EVALUATION_INTERVAL = 35

lstm_model = Sequential()
lstm_model.add(LSTM(64,
                            return_sequences=True,
                            input_shape=x_train_multi.shape[-2:]))
lstm_model.add(LSTM(64, activation='relu'))
lstm_model.add(Dense(12))
lstm_model.compile(optimizer=RMSprop(learning_rate=0.001, rho=0.9), loss='mean_squared_error')

'''for x, y in val_data_multi.take(1):
  print (kickass_lstm_model.predict(x, steps=1).shape)'''

multi_step_history = lstm_model.fit(train_data_multi, epochs=EPOCHS,
                                          steps_per_epoch=EVALUATION_INTERVAL,
                                          validation_data=val_data_multi,
                                          validation_steps=50)


#This is to save the file
'''name = '64lstm-64lstm-12dnse-0001LR-9rho-2'
tname = '64-64-12-0001-9_train'
path = 'graphs/RMS/'''

plot_train_history(multi_step_history, "Multi step history loss and validation loss", path, tname)
for x, y in val_data_multi.take(2):
  multi_step_plot(x[0], y[0], lstm_model.predict(x)[0], 2, path, name)



