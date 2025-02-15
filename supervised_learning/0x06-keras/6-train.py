#!/usr/bin/env python3
"""
6. Early Stopping
"""
import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None, early_stopping=False,
                patience=0, verbose=True, shuffle=False):
    """
    Trains a model using mini-batch gradient descent

    network: model to train
    data: np.ndarray - shape (m, nx) - input data
    labels: one-hot npy.ndarray - shape (m, classes) - labels of data
    batch_size: size of the batch used for mini-batch gradient descent
    epochs: number of passes through data
    validation_data: data to validate the model with, if not None
    early_stopping: boolean indicates whether early stopping should be used
    patience: patience used for early stopping
    verbose: boolean determines if output should be printed during training
    shuffle: boolean determines whether to shuffle the batches every epoch

    Returns: the History object generated after training the model
    """
    callback = []
    if early_stopping and validation_data is not None:
        stop = K.callbacks.EarlyStopping(monitor="val_loss",
                                         patience=patience, mode="min")
        callback.append(stop)

    history = network.fit(data, labels, batch_size=batch_size,
                          epochs=epochs, verbose=verbose, callbacks=callback,
                          validation_data=validation_data, shuffle=shuffle)
    return history
