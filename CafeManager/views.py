from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Welcome to the home page")
    return render(request,'index.html') 

def about(request):
    # return HttpResponse("Learn more about us")
    return render(request, 'about.html') 

def contact(request):
    # return HttpResponse("Contact us here")
    return render(request, 'contact.html')