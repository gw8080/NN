# first neural network with keras make predictions
from numpy import loadtxt
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
option = input ("Do you want to: predict using the saved model or save the model. [predict/save]? : ")

if option == "save":
    # load the dataset
    dataset = loadtxt('testdata.csv', delimiter=',')
    # split into input (X) and output (y) variables
    X = dataset[:,0:8]
    y = dataset[:,8]
    # define the keras model
    model = Sequential()
    model.add(Dense(12, input_dim=8, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    # compile the keras model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # fit the keras model on the dataset
    epochs = int(input("epochs:"))
    model.fit(X, y, epochs=epochs,batch_size=10)
    # evaluate the keras model
    _, accuracy = model.evaluate(X, y)
    print('Accuracy: %.2f' % (accuracy*100))
    model.save("my_prediction_model")



if option == "predict":
    # load the dataset
    dataset = loadtxt('predictdata.csv', delimiter=',')
    # split into input (X) and output (y) variables
    X = dataset[:,0:8]
    y = dataset[:,8]
    # define the keras model
    model = keras.models.load_model("my_prediction_model")
    model = Sequential()
    model.add(Dense(12, input_dim=8, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    # compile the keras model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # fit the keras model on the dataset
    #model.fit(X, y, int(input("epochs:")), batch_size=10, verbose=0)
    # make class predictions with the model
    predictions = (model.predict(X) > 0.5).astype(int)
    # summarize the first 5 cases
    for i in range(5):
        print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))