from django.shortcuts import render, redirect
from sathi import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from adminuser.models import Admins, Report
from django.contrib.auth.models import User
from credentials.cred import firebase, authentication, retrieveDatabase


# Create your views here.


@login_required(login_url = "/admin/adminlogin")
def retrieve_data(request):
        user_id_temp = retrieveDatabase.child("Users").shallow().get().val()  
        Name = []
        Age = []
        Email = []

        for user_id in user_id_temp:
            list_= retrieveDatabase.child("Users").child(user_id).child('Name').get().val()
            Name.append(list_)
        for user_id in user_id_temp:
            list_= retrieveDatabase.child("Users").child(user_id).child('Age').get().val()
            Age.append(list_)
        for user_id in user_id_temp:
            list_= retrieveDatabase.child("Users").child(user_id).child('Email').get().val()
            Email.append(list_)

        user_list = zip(user_id_temp, Name, Age, Email)

        return render(request,'admin/users.html',{'user_list':user_list})


def adminlogin(request):
    if request.user.is_authenticated:
        return redirect('retrieve_data')
    
    return render(request, "admin/adminlogin.html", {})
    
def postadmin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return redirect('retrieve_data')
    else:
        error = "Invalid Login"
        return render(request,"admin/adminlogin.html", {"error":error})
def adminlogout(request):
    auth.logout(request)
    return render(request, 'admin/adminlogin.html')

@login_required(login_url="/admin/adminlogin")
def delete_user(request):
    admin_user = request.user.email
    user_id_to_remove = request.POST.get('user_id')
    retrieveDatabase.child("Users").child(user_id_to_remove).remove()  
    admin_report = Report.objects.create(Action_by = admin_user, Action_to = user_id_to_remove, Action = "Deleted")
    admin_report.save()
    return redirect('retrieve_data')
