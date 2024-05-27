from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np
import cv2
import time
import threading

def load(ep):
	global model
	start = time.time()
	(X_train, y_train), (X_test, y_test) = mnist.load_data()


	X_train = X_train.reshape(X_train.shape + (1,))
	X_test = X_test.reshape(X_test.shape + (1, ))

	X_train = X_train / 255.
	X_test = X_test / 255.


	X_train = X_train.astype(np.float32)
	X_test = X_test.astype(np.float32)

	import tensorflow as tf
	from tensorflow.keras import layers

	model = tf.keras.Sequential([
		layers.Conv2D(filters=10,
					kernel_size=3, 
					activation="relu", 
					input_shape=(28,  28,  1)),
		layers.Conv2D(10,  3, activation="relu"),
		layers.MaxPool2D(),
		layers.Conv2D(10,  3, activation="relu"),
		layers.Conv2D(10,  3, activation="relu"),
		layers.MaxPool2D(),
		layers.Flatten(),
		layers.Dense(10, activation="softmax")
	])

	model.summary()


	model.compile(loss="sparse_categorical_crossentropy", 
				optimizer=tf.keras.optimizers.Adam(),
				metrics=["accuracy"])

	model.fit(X_train, y_train, epochs=ep)

	return time.time()-start
	
def showArr(img):
	output = np.reshape(img, (28, 28))

	plt.matshow(output)
	plt.show()


def showBigArr(img):
	output = np.reshape(img, (280, 280))
	
	output = output.astype(np.float64)

	plt.matshow(output)
	plt.show()


def showImage(img):
    plt.imshow(img, cmap="gray")
    plt.figure(figsize=(3, 3))
    plt.title(img)
    plt.axis(False)
    plt.show()

def predict(image_path):
    # Load the image from file
	img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Resize the image to 28x2	plt.figure(figsize=(3, 3))
	plt.title("280x280 arr")
	plt.axis(False)
    # Convert the array to float32 and normalize the pixel values
	img = img.astype(np.float32)
	img = img / 255.

    # Make a prediction for the image
	predictions = model.predict(img)

    # Get the index of the highest prediction
	
	predicted_number = np.argmax(predictions)

    # Print the predicted number
	return predicted_number


def get(arr):
	arr = arr.split(",")
	arr = compress(arr)

	arr = np.array(arr).reshape(1, 28, 28, 1)
    # Make a prediction
	prediction = model.predict(arr)
    # Get the index of the highest probability
	predicted_number = np.argmax(prediction)
	return predicted_number


def compress(arr):
	#return arr[::100]

	compressed = [[0 for _ in range(28)] for _ in range(28)]

	output = np.reshape(arr, (280, 280))

	for x in range(28):
		for y in range(28):
			avg = 0
			for i in range(10):
				for j in range(10):
					val = float(output[(x*10)+i][(y*10)+j])
					if val > 0.0:
						avg += 1
					else:
						avg += val
			

			comp = avg/100

			if comp > 0.5:
				comp = 1.
			compressed[x][y] = comp

	

	return compressed
		