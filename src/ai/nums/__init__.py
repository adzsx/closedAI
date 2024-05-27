import tensorflow as tf
from tensorflow import keras 
import numpy as np
import time
import os


def load(ep, sq1, sq2):
    global model
    start = time.time()
    model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
    model.compile(optimizer='sgd', loss='mean_squared_error')

    xn, yn = [], []

    for item in sq1.format().split(" "):
        xn.append(float(item))

    for item in sq2.format().split(" "):
        yn.append(float(item))

    xs=np.array(xn)
    ys=np.array(yn)


    model.fit(xs, ys, epochs=ep)

    return time.time()-start


def get(out):
    outn = []
    for n in out.split(" "):
        outn.append(float(n))

    output = model.predict(x=np.array(outn))

    for index, value in enumerate(output):
        print(f"{outn[index]}: {value}")
    
    return output

    out = []
    outn = []


def format(s):
    chars = [",", "-", "_"]

    for char in chars:
        s = s.replace(char, "")
    

    return s

     