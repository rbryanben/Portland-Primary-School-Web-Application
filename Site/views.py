from django.shortcuts import render
from django.http import HttpResponse

#home page 
def homePage(request):
    return render(request,'Site/home/home.html')

def facilitiesPage(request):
    return render(request,'Site/facilities/facilities.html')


def academicsPage(request):
    return render(request,'Site/academics/academics.html')

def galleryPage(request):
    return render(request,"Site/gallery/gallery.html")

def eventsPage(request):
    return render(request,'Site/events/events.html')

def newsPage(request):
    return render(request,'Site/news/news.html')

def admissionsPage(request):
    return render(request,"Site/admissions/admissions.html")