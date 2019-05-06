#Script for dirty data with some jsons that don't have labels 
import scipy.io
import scipy.ndimage
import os
import glob
import numpy as np
import json
import pickle
from sklearn.externals import joblib

#1.Get the paths of the images
#Glob the images and then loop through each image? 

img_files = []

path = '/Users/julianashihadeh/Desktop/Correct_Data_FromGPU2/train'
#Set to current path 

os.chdir(path);
count = 0;
img_files = [];
all_rgb_data = [];
all_meta_data = [];

for x in glob.glob('./*'):
	img_files.append(x.split('/')[1]);

for i in img_files:

	if((i.split('.')[1]) == 'jpg'):
                img = scipy.ndimage.imread(i.split('/')[0], False, mode='RGB');
#               all_rgb_data.append(img[0]);
	if((i.split('.')[1]) == 'json'):
		with open(i) as f:
			meta_data = json.load(f)
			meta_label = meta_data["meta"]["clinical"]["benign_malignant"]
			#try:
			#	meta_label_2 = meta_data["meta"]["clinical"]["diagnosis"]
			if(meta_label == 'benign'):
#                                       print(meta_label)
				value = 0;
			else:
# 					print(meta_label)
				value = 1;
			all_meta_data.append(value);
			count = count + 1;
			all_rgb_data.append(img);
			#except:
                                #print("No diagnosis label")
                                #print("inside the variable:")
                                #print(meta_label_2)
			#	continue;

#next folder
path = '/Users/julianashihadeh/Desktop/Correct_Data_FromGPU2/test'
os.chdir(path);
img_files = [];

for x in glob.glob('./*'):
        img_files.append(x.split('/')[1]);

for i in img_files:
	if((i.split('.')[1]) == 'jpg'):	
		img = scipy.ndimage.imread(i.split('/')[0], False, mode='RGB');
#               all_rgb_data.append(img[0]);
	if((i.split('.')[1]) == 'json'):
		with open(i) as f:
			meta_data = json.load(f)
			meta_label = meta_data["meta"]["clinical"]["benign_malignant"]
			#try:
			#	meta_label_2 = meta_data["meta"]["clinical"]["diagnosis"]
			if(meta_label == 'benign'):
#                                       print(meta_label)
				value = 0;
			else:
#                                       print(meta_label)
				value = 1;
			all_meta_data.append(value);
			count = count + 1;
			all_rgb_data.append(img);
			#except:
                                #print("No diagnosis label")
			#	continue;

rgb_values = np.asarray(all_rgb_data)
labels = np.asarray(all_meta_data)

print(rgb_values.shape);

######
##Training on Randome Forest
######

import scipy.io
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score
#train_data = scipy.io.loadmat('train_32x32.mat')
# extract the images and labels from the dictionary object
print("RGB SHAPE");
print(rgb_values.shape)
X = rgb_values;
print("X SHAPE");
print(X.shape)
y = labels;
# view an image (e.g. 25) and print its corresponding label
img_index = 5
plt.imshow(X[img_index])
plt.show()
print(y[img_index])

from sklearn.utils import shuffle

##Shuffle Round 1
print("Pre vector X length:");
print(len(X));
X = X.reshape(X.shape[1]*X.shape[2]*X.shape[3],X.shape[0]).T
print("Pre vector Y length:");
print(len(y));
y = y.reshape(y.shape[0],)
print("Post vector X length");
print(len(X));
print("Post vector Y length");
print(len(y));
X, y = shuffle(X, y, random_state=42)

print("Passed the shuffle checkpoint");

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
print(clf)

print("Starting the Random Forest Classifier");
RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
           max_depth=None, max_features='auto', max_leaf_nodes=None,
           min_impurity_split=1e-07, min_samples_leaf=1,
           min_samples_split=2, min_weight_fraction_leaf=0.0,
           n_estimators=10, n_jobs=1, oob_score=False, random_state=None,
           verbose=0, warm_start=False)

print("Passed the RFC checkpoint");

from sklearn.model_selection import train_test_split

print("Splitting into the train and test");
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf.fit(X_train, y_train)

tree_pkl_filename = '/Users/julianashihadeh/Desktop/SeniorDesign/code/sklearn-tutorial/project_model_3_pickled.pkl'
tree_model_pkl = open(tree_pkl_filename, 'wb')
joblib.dump(clf,tree_model_pkl)
tree_model_pkl.close()

tree_model_pkl = open(tree_pkl_filename, 'rb')
model = joblib.load(tree_model_pkl)
print("Model pickled. The model's information:")
print(model)

from sklearn.metrics import accuracy_score
preds = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test,preds))
