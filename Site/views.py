from django.shortcuts import render
from django.http import HttpResponse

#home page 
def homePage(request):
    return render(request,'Site/home/home.html')
