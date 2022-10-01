#
# TENSORFLOW GUI PYTHON BACKEND
# A program to simplify training and
# testing AI models created with
# Tensorflow.
# ------------ main.py -----------
# This file is the backend for the GUI that runs 
# and trains the model.
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
#stuff
import os
import sys
from tensorflow import keras
from tensorflow.keras.models import load_model
import utils
print("Program started")
print(str(sys.argv)+" at length "+str(len(sys.argv)))
#for i in range(len(sys.argv)):
#	print(sys.argv[i])
custom = sys.argv[1]
train = sys.argv[2]
model_path = sys.argv[3]
check_point_path = sys.argv[4]
#database_path = sys.argv[5]
minist = sys.argv[5]
epoch = sys.argv[6]
print("IS CUSTOM: "+str(custom))
print("IS TRAINING: "+str(train))
print("IS MINIST: "+str(minist))
#exit()
epoch = int(epoch)
if(int(custom) == 0):
	
	if(int(minist) == 1):
		print("Minist chosen...")
		fashion_mnist = tf.keras.datasets.fashion_mnist

		(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

		class_names = ['T-shirt/top', 'Pants', 'Pullover', 'Dress', 'Coat',
			       'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

		train_images = train_images / 255.0
		test_images = test_images /255.0
else:
	print("Choose an option! Jeez...")
batch_size = 32
if(int(epoch) == 0):
	epoch = 10
if(int(train) == 1):
	model = utils.create_model()
	model.summary()
	checkpoint_path = check_point_path
	checkpoint_dir = os.path.dirname(checkpoint_path)
	cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,save_weights_only=True,verbose=1,save_freq=5*batch_size)

	model.fit(train_images, train_labels,  epochs=epoch,batch_size=batch_size ,validation_data=(test_images, test_labels), callbacks=[cp_callback]) 

	test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)

	model.load_weights(checkpoint_path)
	test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
	print("\n Trained Test Accur:",test_acc)

	model.save(model_path)

else:
	
	print("Loading model...")
	model = utils.loadmodel(str(model_path[0]))
	print("Done..")
	model.summary()
	test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
	print("\n Loaded model Trained Test Accur:",test_acc)
	#input("EXIT ...? ")
