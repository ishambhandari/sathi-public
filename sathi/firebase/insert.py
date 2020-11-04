from firebase import firebase
firebase = firebase.FirebaseApplication("https://sathi-7855d.firebaseio.com/", None)

def print_user():
    result = firebase.get('https://sathi-7855d.firebaseio.com/Users','')
    print(result)

def del_user(usertag):
    firebase.delete('https://sathi-7855d.firebaseio.com/Users/Man', '%s' %usertag)

def del_user_f(usertag_f):
    firebase.delete('https://sathi-7855d.firebaseio.com/Users/Woman', usertag_f)






