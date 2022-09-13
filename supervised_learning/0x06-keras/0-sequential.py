#!/usr/bin/env python3
"""
0. Sequential
"""
import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """
    Builds a neural network with the Keras library

    nx: number of input features to the network
    layers: list containing the number of nodes in each layer of the network
    activations: list containing the activation functions used for each layer
        of the network
    lambtha: L2 regularization parameter
    keep_prob: probability that a node will be kept for dropout

    Returns: keras model
    """
    model = K.Sequential()
    reg = K.regularizers.l2(lambtha)

    for i in range(len(layers)):
        if i == 0:
            model.add(K.layers.Dense(layers[i],
                                     activation=activations[i],
                                     kernel_regularizer=reg,
                                     input_shape=(nx,)))
        else:
            model.add(K.layers.Dropout(rate=(1-keep_prob)))
            model.add(K.layers.Dense(layers[i],
                                     activation=activations[i],
                                     kernel_regularizer=reg))
    return model
