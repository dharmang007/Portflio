from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'MyProfile/includes/home.html') # be careful to put this files in 'templates' folder

def contact(request):
    return render(request,'MyProfile/includes/contact.html', {'content':['If you would like to contact me, please email me','dharmangsolanki999@gmail.com']})

def myArt(request):
    return render(request,'MyProfile/includes/myArt.html')

def myAcademics(request):
    return render(request,'MyProfile/includes/myAcademics.html')

def aboutMe(request):
    return render(request,'MyProfile/includes/aboutMe.html')
