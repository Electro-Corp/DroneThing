import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import matplotlib.pyplot as plt

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
# WHAT TO TRAIN WITH
train_ds = tf.keras.utils.image_dataset_from_directory(data_dir, validation_split=0.2,subset="training",seed=123,image_size=(img_height,img_width),batch_size=batch_size)
# VALIDATE WITH
val_ds = tf.keras.utils.image_dataset_from_directory(data_dir,validation_split=0.2,subset="validation",seed=123,image_size=(img_height, img_width),batch_size=batch_size)
class_names = train_ds.class_names
print(class_names)

# # # # # # # # # # # # # # 
# Create and train model  #
# # # # # # # # # # # # # #
num_classes = 5
def create_model():
	model =  tf.keras.Sequential([
	  tf.keras.layers.Rescaling(1./255),
	  tf.keras.layers.Conv2D(32, 3, activation='relu'),
	  tf.keras.layers.MaxPooling2D(),
	  tf.keras.layers.Conv2D(32, 3, activation='relu'),
	  tf.keras.layers.MaxPooling2D(),
	  tf.keras.layers.Conv2D(32, 3, activation='relu'),
	  tf.keras.layers.MaxPooling2D(),
	  tf.keras.layers.Flatten(),
	  tf.keras.layers.Dense(128, activation='relu'),
	  tf.keras.layers.Dense(num_classes)
])
	model.compile(optimizer='adam',loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),metrics=['accuracy'])	
	return model
def loadmodel(path):
	model = load_model(path)
	return model
model = create_model()


#saving
checkpoint_path = "angle_bracket/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,save_weights_only=True,verbose=1,save_freq=5*batch_size)


model.fit(train_ds,  epochs=3,batch_size=batch_size ,validation_data=val_ds, callbacks=[cp_callback]) 

test_loss, test_acc = model.evaluate(train_ds, verbose=2)

#model.load_weights(checkpoint_path)
test_loss, test_acc = model.evaluate(train_ds, verbose=2)
print("\n Trained Test Accur:",test_acc)

model.save('saved_model/angle_bracket')
model.summary()

probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
predictions = probability_model.predict(train_ds)

predictions
