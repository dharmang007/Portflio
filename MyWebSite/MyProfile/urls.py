from django.urls import re_path,include
from . import views

urlpatterns  = [
    re_path(r'^home/',views.homePage,name='homePage'), # here I am returning the views, u can find this is views.py
    re_path(r'^contact/',views.contact,name= 'contact'),
    re_path(r'^hobbies/',views.myArt,name ='art'),
    re_path(r'^projects/',views.projects),
    re_path(r'^academics/',views.myAcademics,name='academics'),
    re_path(r'^aboutMe/',views.aboutMe),
    re_path(r'^',views.homePage,name='homePage') # keep this element at last so that all the possibilities are tried out first 
]
