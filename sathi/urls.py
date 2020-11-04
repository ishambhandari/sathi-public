from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import home, signin, postsignin, userlogout, signup, postsignup
import adminuser
urlpatterns = [
    #admin site urls
    path('admin/', include('adminuser.urls')),

    path('', home, name='home'),
    path('signin', signin, name='signin'),
    path('welcome/', postsignin, name='welcome'),
    path('logout/', userlogout, name='userlogout'),
    path('signup/', signup, name='signup'),
    path('postsignup/', postsignup, name='postsignup'),


]
