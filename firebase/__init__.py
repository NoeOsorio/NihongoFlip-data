import firebase_admin
import os
from firebase_admin import credentials, firestore

dir_path = os.path.dirname(os.path.realpath(__file__))
cred_path = os.path.join(dir_path, 'cred.json')
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)


db = firestore.client()
