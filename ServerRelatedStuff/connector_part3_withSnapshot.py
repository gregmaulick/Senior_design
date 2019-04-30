#INFO: Files gets all the documents under one collection, adds new data to each document and then prints out all the data
import firebase_admin
from firebase_admin import credentials, firestore
import calendar;
import time;
import threading;

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


#docs = db.collection(u'Users').get() 

#if(docs is None):

#	print("Empty");
#else: 

#	print("Full");

#while( (docs = db.collection(u'Users').get()) is not None)
#	print("data")

# Create a callback on_snapshot function to capture changes
def on_snapshot(col_snapshot, changes, read_time):
#	threading.Timer(5.0, on_snapshot).start()
	print(u'Callback received query snapshot.')
	print(u'Current data ')
#def trying():
#	print("Hello");
#	threading.Timer(1.0, trying).start()
	for change in changes:
		if change.type.name == 'ADDED':
			print(u'New User: {}'.format(change.document.id))
		elif change.type.name == 'MODIFIED':
			print(u'Modified User: {}'.format(change.document.id))
		elif change.type.name == 'REMOVED':
			print(u'Removed User: {}'.format(change.document.id))

while(1):
	print("In the while")
	col_query = db.collection(u'Users')
	# Watch the collection query
	query_watch = col_query.on_snapshot(on_snapshot)
	print("Called snapshot")







#TO GET ALL THE DATA IN THE COLLECTION
#	docs = db.collection(u'Users').get()
#	for doc in docs:
#		#print(u'{} => {}'.format(doc.id, doc.to_dict())) 
		#print(u'{} => '.format(doc.id)) 
#		doc_ref = db.collection(u'Users').document(change.document.id)
		#get the document data and upload into the model here when it comes time to integrating the Ml processing
#		doc_ref.update({
#			u'Classification': validation,
#			u'Date': date,
#		})
		#print(u'{} => {}'.format(doc.id, doc.to_dict())) 
#		print("-----------------------------")
#		print("Document ID")
#		print(u'{}'.format(doc.id)) 
#		print("Document Data")
#		data = doc.to_dict()
#		#For handling images, loop through all the data because i will be what holds the one image
#		#Upload i into the machine learning model
#		#Take the classification and store it into 
#		for i in data.values():
#			print(i)
		#print(data.values())

#except google.cloud.exceptions.NotFound:
#	print(u'No such document!')

