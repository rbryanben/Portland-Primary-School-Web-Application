from django.shortcuts import render
from django.http import HttpResponse
from .models import HomePageContent , KeyPoint, SchoolLevel
from django.core.exceptions import ObjectDoesNotExist

###################################home page 
def homePage(request):
    context = {
        "data" : HomePageContent.objects.get(id=1),
        "keypoints" : KeyPoint.objects.all(),
    }
    #return responce
    return render(request,'Site/home/home.html',context)

def studentLifeLearning(request,level):
    try:
        context = {
            "data" : SchoolLevel.objects.get(level=level)
        }
        return render(request,'Site/home/student-life-learning/student-life-learning.html',context)
    except ObjectDoesNotExist:
        return HttpResponse("This page does not exist")

def keyPointPage(request,id):
    try:
        context = {
            "data" : KeyPoint.objects.get(slug=id)
        }
        return render(request,'Site/home/keypoints/keypoints.html',context)
    except ObjectDoesNotExist:
        return HttpResponse("This page does not exist")

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