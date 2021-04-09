from django.shortcuts import render
from django.http import HttpResponse
from .models import HomePageContent , KeyPoint, SchoolLevel ,NewsItem , FacilitiesPageContent , SchoolFacility , FacilitiesPageContent
from django.core.exceptions import ObjectDoesNotExist

###################################home page 
def homePage(request):
    context = {
        "data" : HomePageContent.objects.get(id=1),
        "keypoints" : KeyPoint.objects.all(),
        "news" : NewsItem.objects.all().order_by('-date_posted')[:10]
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

####### Facilitites 
def facilitiesPage(request):
    try:
        context = {
            "focusedFacilities" : SchoolFacility.objects.all().order_by('-date_posted')[:4],
            "facilities" : SchoolFacility.objects.all(),
            'data' : FacilitiesPageContent.objects.get(id=1)
        }

        return render(request,'Site/facilities/facilities.html',context)
    except:
        return HttpResponse("We ran into a problem while obtaining this page")


def facilitiesViewPage(request,slug):
    context = {
        "data" : SchoolFacility.objects.get(slug=slug)
    }
    return render(request,'Site/facilities/view/view.html',context)

def academicsPage(request):
    return render(request,'Site/academics/academics.html')

def galleryPage(request):
    return render(request,"Site/gallery/gallery.html")

def eventsPage(request):
    return render(request,'Site/events/events.html')

def newsPage(request):
    return render(request,'Site/news/news.html')

def newsViewPage(request,slug):
    try:
        data = NewsItem.objects.get(slug=slug)
        context = {
            "data" : data,
            "points" : data.points.split(","),
        }
        return render(request,"Site/news/view/news_view.html",context)
    except ObjectDoesNotExist:
        return HttpResponse("This page does not exist")

def admissionsPage(request):
    return render(request,"Site/admissions/admissions.html")