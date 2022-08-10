import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
#import tensorflow_datasets as tfds
print(tf.__version__)
import pathlib
# # # # # # # #
# Load Images #
# # # # # # # #
data_dir = pathlib.Path("/home/segfault/GARAGE_STUFF_AI_TRANING")

image_count = len(list(data_dir.glob('*/*.jpg')))

print("IMAGES FOUND: "+str(image_count))
#print("LIST OF IMAGES: "+str(list(data_dir.glob('*/*.jpg'))))

angle_brackets = list(data_dir.glob('angle_bracket/*'))
#PIL.Image.open(str(angle_brackets[0]))

# # # # # # # # # #
# Create dataset  #
# # # # # # # # # #

batch_size = len(angle_brackets)

img_height = 180
img_width = 180

train_ds = tf.keras.utils.image_dataset_from_directory(data_dir, validation_split=0.2,subset="training",seed=123,image_size=(img_height,img_width),batch_size=batch_size)

