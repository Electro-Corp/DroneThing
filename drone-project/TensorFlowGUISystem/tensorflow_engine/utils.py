import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
from tensorflow import keras
from tensorflow.keras.models import load_model
import pathlib
def create_model():
	model = tf.keras.Sequential([
		tf.keras.layers.Flatten(input_shape=(28,28)),
		tf.keras.layers.Dense(128, activation='relu'),
		tf.keras.layers.Dense(10)
	])
	model.compile(optimizer='adam',loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),metrics=['accuracy'])	
	return model
def loadmodel(path):
	try:
		print("Loading "+str(path))
		model = load_model(str(path))
	except OSError:
		print("Error loading model, model does not exist??")
	return model


def createImageDatabasefromImage(path):
	data_dir = pathlib.Path(str(path))
