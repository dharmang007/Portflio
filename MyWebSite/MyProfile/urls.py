from django.urls import path,include
from . import views

urlpatterns  = [
    path('',views.index,name= 'index'), # here I am returning the views, u can find this is views.py

    ]
