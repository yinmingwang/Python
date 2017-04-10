 
import scipy.io as sio
import numpy as np
import sys
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
if __name__ == '__main__':
	mnist_train = sio.loadmat('./mnist_dataset/mnist_train.mat')
	mnist_train_labels = sio.loadmat('./mnist_dataset/mnist_train_labels.mat')
	mnist_test = sio.loadmat('./mnist_dataset/mnist_test.mat')
	mnist_test_labels = sio.loadmat('./mnist_dataset/mnist_test_labels.mat')
	traindataset = mnist_train['mnist_train']
	trainlabels = mnist_train_labels['mnist_train_labels']
	testdataset = mnist_test['mnist_test']
	testlabels = mnist_test_labels['mnist_test_labels']
	bdt = AdaBoostClassifier(base_estimator=RandomForestClassifier())
	bdt.fit(traindataset,trainlabels.ravel())
	predict = bdt.predict(testdataset).reshape(testdataset.shape[0],1)
	score = bdt.score(testdataset,testlabels)
	count = 0
	for i in range(0,predict.shape[0]):
		if predict[i] != testlabels[i]:
			count += 1
	print(count)
	with open('adaboostResult.txt', 'w') as file:
		file.write("ErrorPercent: %f%%\n" %(count / 100))
		file.write("Score: %f\n" %(score))
		file.write("predict testlabel\n")
		for i in range(0, testdataset.shape[0]):
			file.write("%d          %d\n" %(predict[i], testlabels[i]))
            

