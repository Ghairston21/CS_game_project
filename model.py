import tensorflow as tf
from tensorflow import keras
import os
import numpy as np


class TicTacToeModel:

    def __init__(self, numberOfInputs, numberOfOutputs, epochs, batchSize):
        self.epochs = epochs
        self.batchSize = batchSize
        self.numberOfInputs = numberOfInputs
        self.numberOfOutputs = numberOfOutputs
        self.model = tf.keras.Sequential()
        self.model.add(tf.keras.layers.Dense(64, activation='relu', input_shape=(numberOfInputs, )))
        self.model.add(tf.keras.layers.Dense(128, activation='relu'))
        self.model.add(tf.keras.layers.Dense(128, activation='relu'))
        self.model.add(tf.keras.layers.Dense(128, activation='relu'))
        self.model.add(tf.keras.layers.Dense(numberOfOutputs, activation='softmax'))
        self.model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        self.checkpoint_path = "training/weights.ckpt"
        self.checkpoint_dir = os.path.dirname(self.checkpoint_path)
        self.weights_checkpoint = tf.keras.callbacks.ModelCheckpoint(filepath=self.checkpoint_path, save_weights_only=True, verbose=1)

    def train(self, dataset):
        input = []
        output = []
        for data in dataset:
            input.append(data[1])
            output.append(data[0])

        X = np.array(input).reshape((-1, self.numberOfInputs))
        y = tf.keras.utils.to_categorical(output, num_classes=3)
        # Train and test data split
        boundary = int(0.5 * len(X))
        X_train = X[:boundary]
        X_test = X[boundary:]
        y_train = y[:boundary]
        y_test = y[boundary:]
        self.model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=self.epochs, batch_size=self.batchSize, callbacks=self.weights_checkpoint)
    def load(self):
        self.model.load_weights(self.checkpoint_path)

    def predict(self, data, index):
        return self.model.predict(np.array(data).reshape(-1, self.numberOfInputs))[0][index]