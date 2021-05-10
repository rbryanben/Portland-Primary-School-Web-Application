from django.shortcuts import render
from django.http import HttpResponse
from .models import HomePageContent , KeyPoint, SchoolLevel ,NewsItem , FacilitiesPageContent , SchoolFacility , FacilitiesPageContent, AcademicsPageContent,TopStudent , Folder , Image
from .models import Event
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
import json
import datetime

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
    try:
        context = {
            "data" : SchoolFacility.objects.get(slug=slug),   
        }
        return render(request,'Site/facilities/view/view.html',context)
    except:
        return HttpResponse("We ran into a problem while obtaining this page")


def academicsPage(request):
    try:
        context = {
            "data" : AcademicsPageContent.objects.get(id=1),
            "topStudents" : TopStudent.objects.all().order_by("posted")[:4]
        }
        return render(request,'Site/academics/academics.html',context)
    except:
        return HttpResponse("We ran into a problem while obtaining this page")

def galleryPage(request):
    context = {
        "path" : "hey",
    }
    return render(request,"Site/gallery/gallery.html",context)

def galleryFiling(request):
    folder = request.GET['folder']

    #check images 
    hasImages = False
    Images = Image.objects.filter(folder=Folder.objects.get(name=folder))
    if len(Images) > 0 :
        hasImages = True

    #context 
    context = {
        "binary" : Folder.objects.filter(parent=Folder.objects.get(name=folder)),
        "Images" : Images,
        "hasImages" : hasImages,
    }

    return render(request,"Site/gallery/filing/filing.html",context)

def eventsPage(request):
    return render(request,'Site/events/events.html')

@csrf_exempt
def getEvents(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    
    #extract filters 
    fromFilter  = body['from']
    keywords = body["keywords"]
    location = body["location"]


    #if all blank get events starting from that day , returns from here
    if (fromFilter == "" and keywords == "" and location == ""):
        results = Event.objects.filter(DateTimeField__gte=datetime.datetime.today())
        context = {
            "results" : results,
        }
        return render(request,'Site/events/results/event_results.html',context)
    

    #get all items 
    results = Event.objects.all()
    filteredResults = []

    

    #filter
    if keywords != "":
        #filter loop
        for event in results:
            if (keywords.lower() in event.event.lower()):
                filteredResults.append(event)
        #re-assign results and clear results
        results = filteredResults
        filteredResults = []

    
    #location 
    if location != "":
        #filter loop
        for event in results:
            if (location.lower() in event.location.lower()):
                filteredResults.append(event)
        #re-assign results and clear results
        results = filteredResults 
        filteredResults = []



    if fromFilter != "":
        givenDate = datetime.datetime.strptime(fromFilter, '%Y-%m-%d')
        #filter loop
        for event in results:
            dateStripped = event.DateTimeField.strftime('%Y-%m-%d')
            dateStripped = datetime.datetime.strptime(dateStripped, '%Y-%m-%d')

            if (givenDate == dateStripped):
                filteredResults.append(event)
               
        #re-assign results and clear results
        results = filteredResults 
        filteredResults = []


    context = {
        "results" : results,
    }
    return render(request,'Site/events/results/event_results.html',context)

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