#!/usr/bin/env python3
"""
Module for class NeuralNetwork
"""
import numpy as np


class NeuralNetwork:
    """
    Defines a neural network with one hidden layer
    performing binary classification
    """

    def __init__(self, nx, nodes):
        """
        Class Constructor

        nx is the number of input features
        nodes is the number of nodes found in the hidden layer
        """
        if type(nx) != int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(nodes) != int:
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")
        self.__W1 = np.random.randn(nodes, nx)
        self.__b1, self.__b2 = np.zeros((nodes, 1)), 0
        self.__A1, self.__A2 = 0, 0
        self.__W2 = np.random.randn(1, nodes)

    @property
    def W1(self):
        """ Getter for W1 """
        return self.__W1

    @property
    def b1(self):
        """ Getter for b1 """
        return self.__b1

    @property
    def A1(self):
        """ Getter for A1 """
        return self.__A1

    @property
    def W2(self):
        """ Getter for W2 """
        return self.__W2

    @property
    def b2(self):
        """ Getter for b2 """
        return self.__b2

    @property
    def A2(self):
        """ Getter for A2 """
        return self.__A2
