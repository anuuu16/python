from sklearn import datasets
import cv2,dlib,sys
import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import pandas as pd
# iris = datasets.load_iris()
# print(iris)
def display_image(image_array):
    cv2.imshow("image",image_array)
    cv2.waitKey()

iris = datasets.load_iris()  
# digits = datasets.load_digits()
# img = digits.images[0]
# res = cv2.resize(img,None,fx=50, fy=50, interpolation = cv2.INTER_AREA)
# win = dlib.image_window()
# win.set_image(res)
# display_image(res)
data1 = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])
x = np.random.RandomState(0).rand(2000)
X = np.array(x, dtype='float32').reshape(50,40)
display_image(cv2.resize(X,None,fx=20, fy=20, interpolation = cv2.INTER_AREA))

ax1 = data1.plot.scatter(x='target', y='target',c='target')