from django.urls import path
from myapp import views
from django.contrib import admin
urlpatterns = [
    path('admin_login/',views.ad_login,name='admin_login'),
    path('create_user/',views.create_user,name='create_user'),
    path('user_login/',views.user_login,name='user_login')
]
