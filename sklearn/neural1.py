# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 14:16:16 2021

MLP = Multi Layer Perceptron

@author: gvige
"""

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.neural_network import MLPClassifier

# Load data
digits = datasets.load_digits()
n_samples = len(digits.images)
data = digits.images.reshape((n_samples,-1))

# Learn ie fit
X,y = data[:n_samples//2], digits.target[:n_samples//2]
# alpha = L2 penalty (regularization term) parameter.
classifier = MLPClassifier(solver='lbfgs', alpha=1e-10, hidden_layer_sizes=(5, 2), random_state=1)
classifier.fit(X, y)

# Predict and plot
for index, image in enumerate(digits.images[n_samples//2:n_samples//2+4]):
	plt.subplot(1,4,index+1)
	plt.imshow(image, cmap=plt.cm.gray_r)
	plt.title('Prediction: %i' % classifier.predict(image.reshape((1,64))), fontsize=10)