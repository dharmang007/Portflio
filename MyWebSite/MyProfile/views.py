from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'MyProfile/includes/home.html') # be careful to put this files in 'templates' folder

def contact(request):
    return render(request,'MyProfile/includes/')
