from django.contrib import admin
from django.urls import path, include
from . import views 
from .forms import NewUserForm
from django.contrib import messages
from .views import profile

urlpatterns = [
   path('index', views.index, name='index' ),
    path('add/', views.add, name='add' ),
    path('<id>/delete', views.delete_view, name='del'),
    path('<id>/update', views.update_view, name='up' ),
    path('', views.base, name='base'),
    path("login", views.login_request, name="login"), 
    path("register", views.register_request, name="register"), 
    path("logout", views.logout_request, name= "logout"),
    path('profile', views.profile, name='profile'),
    path('EditProfile/', views.EditProfile, name='edit'),
    path('about', views.about, name='about'),
   # path('app', views.app, name='app'),


   

   
    
 
    
      
]