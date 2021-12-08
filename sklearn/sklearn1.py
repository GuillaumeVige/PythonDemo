# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 16:42:08 2021
D'apres une video d'Alexandre GRAMFORT
https://www.youtube.com/watch?v=ZD5lJGq1rvQ&ab_channel=BlendWebMix

@author: GVIGE
"""
import matplotlib.pyplot as plt
from sklearn import datasets, svm

# Load data
digits = datasets.load_digits()
n_samples = len(digits.images)
data = digits.images.reshape((n_samples,-1))

# Learn ie fit
classifier = svm.SVC()
classifier.fit(data[:n_samples//2], digits.target[:n_samples//2])

# Predict and plot
for index, image in enumerate(digits.images[n_samples//2:n_samples//2+4]):
	plt.subplot(1,4,index+1)
	plt.imshow(image, cmap=plt.cm.gray_r)
	plt.title('Prediction: %i' % classifier.predict(image.reshape((1,64))), fontsize=10)