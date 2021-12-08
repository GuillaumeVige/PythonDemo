# -*- coding: utf-8 -*-
"""
Created on Fri Nov  19 10:42:08 2021

Reconnaissance de chiffres par KNN

@author: GVIGE
"""
import matplotlib.pyplot as plt
from sklearn import neighbors, datasets

# Load data
digits = datasets.load_digits()
n_samples = len(digits.images)
data = digits.images.reshape((n_samples,-1))

# Learn ie fit
X,y = data[:n_samples//2], digits.target[:n_samples//2]
classifier = neighbors.KNeighborsClassifier(n_neighbors=15, weights='distance').fit(X,y)

# Predict and plot
for index, image in enumerate(digits.images[n_samples//2:n_samples//2+4]):
	plt.subplot(1,4,index+1)
	plt.imshow(image, cmap=plt.cm.gray_r)
	plt.title('Prediction: %i' % classifier.predict(image.reshape((1,64))), fontsize=10)