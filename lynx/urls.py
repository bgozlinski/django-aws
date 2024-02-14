from django.urls import path
from . import views

app_name = 'lynx'

urlpatterns = [
    path('', views),

]