from django.urls import re_path,include
from . import views

urlpatterns  = [
    re_path(r'^home/',views.index,name= 'home'), # here I am returning the views, u can find this is views.py
    re_path(r'^contact/',views.contact,name= 'contact'),
    re_path(r'^myArt/',views.myArt,name ='art'),
    re_path(r'^myAcademics/',views.myAcademics,name='academics'),
    re_path(r'^aboutMe/',views.aboutMe),
    re_path(r'^',views.index,name='index') # keep this element at last so that all the possibilities are tried out first 
    ]
