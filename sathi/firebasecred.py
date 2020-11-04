from google.auth.transport.requests import Request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred=credentials.Certificate('cred.json')
firebase_admin.initialize_app(cred, {
    'databaseURL':'https://sathi-7855d.firebaseio.com'
})

ref = db.reference('User')
user=ref.child('Man')
print(user)