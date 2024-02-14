from django.urls import path
from . import views

app_name = 'lynx'


urlpatterns = [
    path('', views.index, name=''),
    path('register', views.register, name='register'),
    path('my-login', views.my_login, name='my-login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile-management', views.profile_management, name='profile-management'),

]
