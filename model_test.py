import scipy.io
import scipy.ndimage
import matplotlib.pyplot as plt
import json
import pickle
from sklearn.externals import joblib
import numpy as np
from flask import Flask
import firebase_admin
from firebase_admin import credentials, firestore
import calendar;
import time;
import threading;

app = Flask(__name__)

#cred = credentials.Certificate("/Users/julianashihadeh/Desktop/PythonAdminAccessToSeniorDesignApp/my-new-app-2019-firebase-adminsdk-v9240-16975dd992.json")
#firebase_admin.initialize_app(cred)
#db = firestore.client();

tree_pkl_filename = '/Users/julianashihadeh/Desktop/SeniorDesign/code/sklearn-tutorial/project_model_3_pickled.pkl'
##getting our trained model from a file we created earlier

tree_model_pkl = open(tree_pkl_filename, 'rb')
model = joblib.load(tree_model_pkl)
print(model)

@app.route("/")
def classify():

#	def on_snapshot(col_snapshot, changes, read_time):
        	#print(u'Callback received query snapshot.')
        	#print(u'Current data ')
#		checked = "Yes"
#		for change in changes:
#			if change.type.name == 'ADDED':
                	        #print(u'New User: {}'.format(change.document.id))
#				added = "True"


#       print("In the while")
#	col_query = db.collection(u'Users')
        # Watch the collection query
#	query_watch = col_query.on_snapshot(on_snapshot)

#        print("Called snapshot")


	#tree_pkl_filename = '/Users/julianashihadeh/Desktop/SeniorDesign/code/sklearn-tutorial/project_model_3_pickled.pkl'
	#getting our trained model from a file we created earlier

	#tree_model_pkl = open(tree_pkl_filename, 'rb')
	#model = joblib.load(tree_model_pkl)
	#print(model)
	
	#i = '/Users/julianashihadeh/Desktop/Correct_Data_FromGPU2/test/ISIC_0000539.jpg'
	i = '/Users/julianashihadeh/Desktop/Correct_Data_FromGPU2/test/ISIC_0000008.jpg'
	img = scipy.ndimage.imread(i, False, mode='RGB');
	label = '/Users/julianashihadeh/Desktop/Correct_Data_FromGPU2/test/ISIC_0000008.json'

	with open(label) as f:
	        meta_data = json.load(f)
	        meta_label =  meta_data["meta"]["clinical"]["benign_malignant"]
	
#	print(meta_label)
#	plt.imshow(img)
#	plt.show()

	from sklearn.metrics import accuracy_score

	#print("The image shape")
	#print(img.shape)
	X = img;
	#print("The X variable shape")
	#print(X.shape)
	#print("Reshaping X")
	X = X.reshape(X.shape[0]*X.shape[1]*X.shape[2]).T
	#print("The X value reshaped")
	#print(X.shape)
	X = X.reshape(1, -1)
	#print(X.shape)
	##print(model.predict(X))
	result = model.predict(X)
	if(result[0] == 0):
		result = "Benign"
	#	return "Benign";
	else:
		result = "Malignant"
	#	return "Malignant";
	info = (meta_label, result);

	return info;

#Once we open this to users, this should be turned off??
if __name__ == '__main__':
	app.run(debug = True)


