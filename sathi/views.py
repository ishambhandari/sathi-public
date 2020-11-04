from django.shortcuts import render,redirect
import pyrebase
from django.contrib import auth
from firebase import firebase
from django.contrib.auth import views as views_auth
from credentials import cred




# creddata={
#   "type": "service_account",
#   "project_id": "sathi-7855d",
#   "private_key_id": "5dd8079b6e497623b1c3d437f4aee66096569402",
#   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDhYjncqDSl+F0A\n5zmwWKVGv6tlXDcURZch+WlY1V7nCiWzdO+YCuyOA4ZnkG3fSkJz29qM6OtkIXLf\nMzwDJNjjDObKM85Cu9MazzzjcABGQfpGSHnclb6jTniiWKQGAGS8RAM37b9sDJ7j\nVd64yWHP5KhXeKfMS5OUYOoBNO3d70zi8B6VdfZEfvqSWvBt/+IdHXD520j+8Ec9\njoRQ8ZYTJ68N+iW1sPO4AeZ9IWepHS48ZkxqXx12VIt0YvbNZmiisHMSLpBznvCo\ntWi+A87yl3mVrzviZz9xFxaFRDEE75fbLVWp17QW6Vtffl7fytQVkWZ1HwnbCuy1\nzkqcRP49AgMBAAECggEAElhy+kWMx4ewVk778KE+jsQyONVpPFKvyxmonAz+JRM7\n32Ag0oDtIWAjFBH7B4ZdY13da8PXyTY5yfY7J8xbhRu7O3E9FEyCkfeVbrPiqdVc\nAFWM6cockuFjy18otr5YdMSaeHZ3Mt3SHxIRx3vI5OmpVDljeysZr6W11nRO+lYF\nkuqgU93EUV1RkkjTw+Zkj2bvxU3qLXaVzD93QuxNZnQVVXh+5oXYgIfujS6Ji5LV\nIA3nbxmMmjCMMHROpcehhckM4owT3B3EvmBMxLVZyg7rmuUrLEZn8/APmwtCFZ7d\nPBpUsKk3c7IhTNmX8MbkANJ65qc8XHoErPObsTKJMQKBgQDwVPu5+9djJIhgkmPg\nd0JsMqeOGEvKaS0tsW9Z1qSmpU8ZYMTo4Z4Kvj3XzQK7r4PQ3TofQwlbhEqMTS4B\nw950HQIhI299wjnG9dSI/ssYKG6Se822kkFyqegtMCo5retuevI/Iyw0vsWM6RDH\n/o1rT9Q4bGHZi7HaYZhZKf2qJQKBgQDwE8OHJyLNCrisl0HBcS1+d8QHY7kgUMO8\nMRjUs6s+PVRV98q1BGlWhIG1Oua0gwXcBYC14CSz34IGNR+9rVqXL8a26/0gvpww\nh8H8X08NoYzz+JxvxLv/Aa6Jlp0XYPPaJZWhT+T1nl5al8kv+PqSCH5BP15WNiKe\nxYxdhzDsOQKBgQCeQhgRfLl029XCYiPK6D2hKioT9APUojXR5QnCSwnZgvn3aDXC\ndO+xe10WAjZOiWFv5H4ln+tFjHPat+gX2XdfVsrUL5V3ZrLNRYxTOhVbLyTA6S2p\nj93xN9lgCFuF5/Ukp2lmEi9F/GnyRHd8ey98/vBsx1IYA1l2yNWdwXz80QKBgF8v\ndtafLa0eExpa3jdUKDV8RrynTT8CxphW3wF2Ou7yYf2zwSsEFL+4ybSRJedsC2aw\nx9dUhzjJ5UOQzITntoM67g6YgkP5TvPu33qwTyeYZcpVR7EIz4DLqefjT2V1izly\nrWDHzH+VytMgWyQqEy7TLzuvZDfKPu+0Y3KxpzQBAoGAXDPKCBTXn6ZQyG403YKt\nv6HcUZv8NIENFDHEyHbAvxaDCeKlE3derxFnmvxhafHVFYLjVpy5tAeQpM1jD7jJ\nOlEQG+FjXXrVbmQJ1KQt+0nXe2wwOavX9mRrqr9hbNxTBtyr+xrv9+ks3lQr155D\neQMKgPx/FEWQE7//N3itWyQ=\n-----END PRIVATE KEY-----\n",
#   "client_email": "firebase-adminsdk-1ac1t@sathi-7855d.iam.gserviceaccount.com",
#   "client_id": "111973346925804974041",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-1ac1t%40sathi-7855d.iam.gserviceaccount.com"
# }


# config = {
   
#     'apiKey': "AIzaSyBmACm1iYZkQOzfSYmOlzHzS22pTdGkCFQ",
#     'authDomain': "sathi-7855d.firebaseapp.com",
#     'databaseURL': "https://sathi-7855d.firebaseio.com",
#     'projectId': "sathi-7855d",
#     'storageBucket': "sathi-7855d.appspot.com",
#     'messagingSenderId': "1085368744685",
#     'appId': "1:1085368744685:web:e54fd4d72e9b2e823faae4",
#     'measurementId': "G-S5RDQF37XR"
#   }

# firebase = pyrebase.initialize_app(config)

# authentication = firebase.auth()    

# retrieveDatabase = firebase.database()

def home(request):
    return render(request,'home.html',{})

def signin(request):
    return render(request,'signin.html',{})

def postsignin(request):
    email = request.POST.get('email')
    passwd = request.POST.get('password')
    try:
        user = authentication.sign_in_with_email_and_password(email, passwd)
    except:
        message = "invalid login"
        return render(request,"signin.html",{'message': message})
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, 'welcome.html', {"Email": email})

def userlogout(request):
    auth.logout(request)
    return render(request, 'signin.html')


def signup(request):
    return render(request, 'signup.html')

def postsignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    gender = request.POST.get('gender')

    user = authentication.create_user_with_email_and_password(email, password)
    uid = user['localId']
    data = {
        "Name":name,
        "Email" : email
    }

    if gender == "male": 
        gen = "Man"
    else:
        gen = "Woman"
    firebase.database().child("Users").child(uid).set(data)
    return render(request, 'signin.html')






