
#from keras.layers.core import Dense, Activation, Dropout
#from keras.layers.recurrent import LSTM

from keras.layers import LSTM
from tensorflow.keras.layers import LSTM,Dropout,Dense
from keras.models import Sequential
import lstm, time #helper libraries


def stock_predict():
    X_train, y_train, X_test, y_test = lstm.load_data('sp500.csv', 50, True)

    #Step 2 Build Model
    model = Sequential()


    model.add(LSTM(units=50,return_sequences=True,input_shape=(X_train.shape[1],1)))
    model.add(Dropout(0.2))

    model.add(LSTM(
      100,
      return_sequences=False))
    model.add(Dropout(0.2))

    model.add(Dense(1, activation='linear'))

    start = time.time()
    model.compile(loss='mse', optimizer='rmsprop')
    print ('compilation time : ', time.time() - start)

    #Step 3 Train the model
    model.fit(
        X_train,
        y_train,
        batch_size=512,
        epochs=1,
        validation_split=0.05)

    #Step 4 - Plot the predictions!
    predictions = lstm.predict_sequences_multiple(model, X_test, 50, 50)
    lstm.plot_results_multiple(predictions, y_test, 50)