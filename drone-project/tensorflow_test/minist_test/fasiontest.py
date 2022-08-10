#fasion mnist dataset thing
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
print(tf.__version__)
def create_model():
	model = tf.keras.Sequential([
		tf.keras.layers.Flatten(input_shape=(28,28)),
		tf.keras.layers.Dense(128, activation='relu'),
		tf.keras.layers.Dense(10)
	])
	model.compile(optimizer='adam',loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),metrics=['accuracy'])	
	return model
def load_model(path):
	model = tf.keras.load_model(path)
	return model
# load data set
fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Pants', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0
test_images = test_images /255.0

#variables
batch_size = 32

#create model

model = create_model()
model.summary()

#saving
checkpoint_path = "fashion_model/checkpoints/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,save_weights_only=True,verbose=1,save_freq=5*batch_size)


model.fit(train_images, train_labels,  epochs=50,batch_size=batch_size ,validation_data=(test_images, test_labels), callbacks=[cp_callback]) 

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)

model.load_weights(checkpoint_path)
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print("\n Trained Test Accur:",test_acc)

model.save('saved_model/fashion')
#untrained
untrainedmodel = create_model()
un_test_loss, un_test_acc = untrainedmodel.evaluate(test_images, test_labels, verbose=2)
print("\n Trained Test Accur:",un_test_acc)
#predictions
probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
predictions = probability_model.predict(test_images)

#display
def plot_image(i, predictions_array, true_label, img):
  true_label, img = true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

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
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')
i = 0
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i, predictions[i], test_labels, test_images)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions[i], test_labels)
plt.tight_layout()
plt.show()

