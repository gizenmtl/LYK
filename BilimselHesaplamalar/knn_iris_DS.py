from sklearn import datasets, neighbors #sklearn string veri içermez.
import numpy as np
#Load iris data from 'dataset module'
iris=datasets.load_iris()
#Get data-records and record-labels in arrays X and y
X=iris.data #notasyonda bu şekilde olduğu için. input olan x büyük yazılır. class olan y de küçük yazılır.
y=iris.target
#Create an instance of KNeighborsClassifier and then fit training data
clf=neighbors.KNeighborsClassifier()
clf.fit(X,y) #eğitilmiş halini bu objeye yazıyor.
#Make class predictions for all observations in X
Z=clf.predict(X)
#Compare predicted class labels with actual class label
accuracy=clf.score(X,y)
print("predicted model accuracy: "+str(accuracy))
#Add a row of predicted classes to y-array for ease of comparison
A=np.vstack([y,Z])
print(A)
