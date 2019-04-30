#INFO: Files gets all the documents under one collection, adds new data to each document and then prints out all the data
import firebase_admin
from firebase_admin import credentials, firestore
import calendar;
import time;

#Setting up the connection to the Firebase Database for our app
cred = credentials.Certificate("/Users/julianashihadeh/Desktop/PythonAdminAccessToSeniorDesignApp/my-new-app-2019-firebase-adminsdk-v9240-16975dd992.json")
firebase_admin.initialize_app(cred)
db = firestore.client();


#Unpickle the model when it comes time to add it in



#Reading and saving data 

#Setting up the variables to add
validation = "true"
ts = time.gmtime()
date = time.strftime("%Y-%m-%d %H:%M:%S", ts)

try:
#TO GET ONE DOCUMENT
#	doc_ref = db.collection(u'Users').document('A');
#	doc = doc_ref.get();
#	print(doc)
#	print(doc['connection']);
#	print(u'Document data')

#	print(format(doc.to_dict()))
#	print(u'Document data: {}'.format(doc.to_dict()))

#TO GET ALL THE DATA IN THE COLLECTION
	docs = db.collection(u'Users').get()
	for doc in docs:
		#print(u'{} => {}'.format(doc.id, doc.to_dict())) 
		#print(u'{} => '.format(doc.id)) 
		doc_ref = db.collection(u'Users').document(doc.id)
		#get the document data and upload into the model here when it comes time to integrating the Ml processing
		doc_ref.update({
			u'Classification': validation,
			u'Date': date,
		})
		#print(u'{} => {}'.format(doc.id, doc.to_dict())) 
		print("-----------------------------")
		print("Document ID")
		print(u'{}'.format(doc.id)) 
		print("Document Data")
		data = doc.to_dict()
		#For handling images, loop through all the data because i will be what holds the one image
		#Upload i into the machine learning model
		#Take the classification and store it into 
		for i in data.values():
			print(i)
		#print(data.values())

except google.cloud.exceptions.NotFound:
	print(u'No such document!')

