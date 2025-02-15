#!/usr/bin/env python3
"""
1. Crop
"""
import tensorflow as tf


def crop_image(image, size):
    """
    Performs a random crop of an image

    Args:
        image: 3D tf.Tensor containing the image to crop
        size: tuple containing the size of the crop

    Returns: cropped image
    """
    return tf.image.random_crop(image, size)
