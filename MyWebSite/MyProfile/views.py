from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePage(request):

    return render(request,'MyProfile/home.html') # be careful to put this files in 'templates' folder

def contact(request):
    return render(request,'MyProfile/contact.html', {'content':['If you would like to contact me, please email me','dharmangsolanki999@gmail.com']})

def myArt(request):
    return render(request,'MyProfile/myArt.html')

def myAcademics(request):
    return render(request,'MyProfile/myAcademics.html')

def aboutMe(request):
    return render(request,'MyProfile/aboutMe.html')

def projects(request):
    return render(request,'MyProfile/projects.html')

