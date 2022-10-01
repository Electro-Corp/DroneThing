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
data_dir = pathlib.Path("/home/segfault/foodbank")

image_count = len(list(data_dir.glob('*/*.jpg')))

print("IMAGES FOUND: "+str(image_count))
#print("LIST OF IMAGES: "+str(list(data_dir.glob('*/*.jpg'))))

full = list(data_dir.glob('full/*'))
empty = list(data_dir.glob('empty/*'))
#PIL.Image.open(str(angle_brackets[0]))

# # # # # # # # # #
# Create dataset  #
# # # # # # # # # #

batch_size = len(full) + len(empty)

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
checkpoint_path = "foodbank/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,save_weights_only=True,verbose=1,save_freq=5*batch_size)


model.fit(train_ds,  epochs=50,batch_size=batch_size ,validation_data=val_ds, callbacks=[cp_callback]) 

test_loss, test_acc = model.evaluate(train_ds, verbose=2)

#model.load_weights(checkpoint_path)
test_loss, test_acc = model.evaluate(train_ds, verbose=2)
print("\n Trained Test Accur:",test_acc)

model.save('saved_model/foodbank')
model.summary()

probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
predictions = probability_model.predict(train_ds)


#display
def plot_image(i, predictions_array, true_label, img):
  true_label, img = true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow((img * 255), cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)
def plot_value_array(i, predictions_array, true_label):
  true_label = true_label[i]
  plt.grid(False)
  plt.xticks(range(10))
  plt.yticks([])
  #thisplot = plt.bar(range(10), predictions_array, color="#777777")
  #plt.ylim([0, 1])
  #predicted_label = np.argmax(predictions_array)

  #thisplot[predicted_label].set_color('red')
  #thisplot[true_label].set_color('blue')
i = 0
train_ds = train_ds.unbatch()
images = list(train_ds.map(lambda x, y: x)) 
labels = list(train_ds.map(lambda x, y: y))

print(len(labels))
print(len(images))
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i, predictions[i], labels, images)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions[i], labels)
plt.tight_layout()
plt.show()
