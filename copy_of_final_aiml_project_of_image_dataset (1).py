# -*- coding: utf-8 -*-
"""Copy of FINAL AIML PROJECT OF IMAGE DATASET.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UfwkFvXwAfuKHwxdlmKLNXQ1H48z1o-C
"""

from google.colab import drive

# Mount Google Drive to access the dataset
drive.mount('/content/drive')

import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
labels = ['diseased cotton leaf','fresh cotton leaf']
img_size = 200
data = []
def get_training_data(data_dir):
  for label in labels:
    path=os.path.join (data_dir, label)
    class_num = labels.index(label)
    print(class_num)
    for img in os.listdir (path):
      try:
        
        img_arr = cv2.imread(os.path. join (path, img), cv2.COLOR_BAYER_GB2RGB)
        #print(img_arr.shape)
        resized_arr = cv2.resize(img_arr, (img_size, img_size))
        data.append ([resized_arr, class_num])
      except Exception as e:
        print(e)
    
  return np.array(data)


train = get_training_data('/content/drive/MyDrive/train')
print(data)
for i in range(0,10):
  plt.imshow(data[i][0])
  print(data[i][0])

for label in labels:
  print(labels.index(label))

#print(train[300][1])

x=[]
y=[]
#0 means diseased
#1 means Normal
count=0
for i in range(len(train)):
  if train[i][1]==0:
    x.append(train[i][0:2])
  else:
    y.append(train[i][0:2])
    count=count+1
print(count)
y

#this code is used to find the no of images in each label
dise=0
nond=0
for i,j in train:
  if j==0:
    dise=dise+1
  else:
    nond=nond+1
print(dise,nond)

x

x=[]
y=[]
for i,j in data:
  x.append(i)
  y.append(j)

y

x

"""LOGISTIC REGRESSION"""

from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = 0.25, random_state = 47)

xtrain

import numpy as np

x=np.array(x).reshape(1951,120000)
x

print(np.array(xtrain).shape)

print(np.array(ytest).shape)

x1=np.array(x).shape

x1

x

y1=np.array(y).shape
y1

d=np.array(xtrain).reshape(1463,120000)
d

e=np.array(xtest).reshape(488,120000)
e

print(np.asarray(d.shape))

from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
d= sc_x.fit_transform(d)#normalizing
e = sc_x.transform(e)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(random_state = 0)

model.fit(d, ytrain)

y_pred=model.predict(e)
y_pred

from sklearn.metrics import accuracy_score
print ("Accuracy : ", accuracy_score(ytest,y_pred))

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(ytest,y_pred)
print("Confusion matrix:\n",cm)

from sklearn.metrics import accuracy_score
print("Accuracy:",accuracy_score(ytest,y_pred))

"""KNN"""

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=16)#k value

knn.fit(d,ytrain)

y_pred = model.predict(e)
y_pred

print("predicted value for training value",knn.score(d,ytrain))
print("predicted value for testing value",knn.score(e,ytest))
print("Overall Accuracy:",knn.score(sc_x.transform(x),y))

y_pred=knn.predict(e)
y_pred

from sklearn.metrics import accuracy_score
print ("Accuracy : ", accuracy_score(ytest,y_pred))

from sklearn.metrics import confusion_matrix
knns=confusion_matrix(ytest,y_pred)
print("Confusion matrix:\n",knns)

"""CROSS VAILDATION

Naive Bayes Classifier
"""

from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()

nb.fit(d,ytrain)

import numpy as np
print("Training Accuracy",nb.score(d,ytrain))
print("Testing Accuracy",nb.score(e,ytest))
print("Overall Accuracy:",nb.score(sc_x.transform(x),y))

y_pred=nb.predict(e)
y_pred

from sklearn.metrics import accuracy_score
print ("Accuracy : ", accuracy_score(ytest,y_pred))

from sklearn.metrics import confusion_matrix
nbb=confusion_matrix(ytest,y_pred)
print("Confusion matrix:\n",nbb)

"""SUPPORT VECTOR MACHINE"""

from sklearn import svm
SVM= svm.SVC()

SVM.fit(d, ytrain)

print("Training Accuracy",SVM.score(d,ytrain))
print("Testing Accuracy",SVM.score(e,ytest))
print("Overall Accuracy:",SVM.score(sc_x.transform(x),y))

y_pred=SVM.predict(e)
y_pred

from sklearn.metrics import confusion_matrix
SVMS=confusion_matrix(ytest,y_pred)
print("Confusion matrix:\n",SVMS)

"""Decision Tree Classifier"""

from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier()

dtc.fit(d,ytrain)

print("Training Accuracy",dtc.score(d,ytrain))
print("Testing Accuracy",dtc.score(e,ytest))
print("Overall Accuracy:",dtc.score(sc_x.transform(x),y))

y_pred=dtc.predict(e)
y_pred

from sklearn.metrics import confusion_matrix
dtcs=confusion_matrix(ytest,y_pred)
print("Confusion matrix:\n",dtcs)

"""RANDOMFOREST"""

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()

rfc.fit(d,ytrain)

print("Training Accuracy",rfc.score(d,ytrain))
print("Testing Accuracy",rfc.score(e,ytest))
print("Overall Accuracy:",rfc.score(sc_x.transform(x),y))

y_pred=rfc.predict(e)
y_pred

from sklearn.metrics import confusion_matrix
rfcs=confusion_matrix(ytest,y_pred)
print("Confusion matrix:\n",rfcs)

from sklearn.metrics import accuracy_score
accuracy_model = accuracy_score(y,model.predict(sc_x.transform(x)))
print("Logistic regression:",accuracy_model)
accuracy_nb = accuracy_score(y,nb.predict(sc_x.transform(x)))
print("navie bayes;",accuracy_nb)
accuracy_knn = accuracy_score(y,knn.predict(sc_x.transform(x)))
print("KNN:",accuracy_knn)
accuracy_SVM = accuracy_score(y,SVM.predict(sc_x.transform(x)))
print("Support vector machine:",accuracy_SVM)
accuracy_dtc = accuracy_score(y,dtc.predict(sc_x.transform(x)))
print("Descision tree:",accuracy_dtc)
accuracy_rfc = accuracy_score(y,rfc.predict(sc_x.transform(x)))
print("Random forest:",accuracy_rfc)

import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

algo = ['logistic reg','Naive bayes','knn clf','SVM','decision tree','random forest']

accuracy = [accuracy_model*100,accuracy_nb*100,accuracy_knn*100,accuracy_SVM*100,accuracy_dtc*100,accuracy_rfc*100]

ax.bar(algo[0],accuracy[0],color = 'b')

ax.bar(algo[1],accuracy[1],color = 'y')

ax.bar(algo[2],accuracy[2],color = 'pink')


ax.bar(algo[3],accuracy[3],color = 'green')

ax.bar(algo[4],accuracy[4],color = 'r')

ax.bar(algo[5],accuracy[5],color = 'orange')

plt.xlabel('Classifiers------------>')

plt.ylabel('Accuracies------------->')

plt.title('ACCURACIES RESULTED')

plt.show()

from google.colab import drive
drive.mount('/content/drive')