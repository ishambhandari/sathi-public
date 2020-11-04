from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from adminuser.views import retrieve_data, adminlogin, postadmin, adminlogout, delete_user

urlpatterns = [
    path('adminlogin/',adminlogin, name='adminlogin'),
    path('postadmin/', postadmin, name='postadmin'),
    path('superadmin/', admin.site.urls),
    path('adminpage/', retrieve_data, name='retrieve_data'),
    path('adminlogout/', adminlogout, name='adminlogout'),
    path('del/', delete_user, name='del'),
]