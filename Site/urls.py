from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homePage,name="Home"), # Home-page
    path('facilities/',views.facilitiesPage,name="Facilities"),  #Facilities
    path('academics/',views.academicsPage,name="Academics"),  #Academics
    path('gallery/',views.galleryPage,name="Gallery"), #Gallery
    path('events/',views.eventsPage,name="Events"), #Events
    path('news/',views.newsPage,name="News"), #News
    path('admissions/',views.admissionsPage,name="Admissions"), #Admissions

    #subpages gallery
    path('gallery/filing/',views.galleryFiling,name="filing_system"),

    #subpages home
    path('keypoints/<str:id>',views.keyPointPage,name="Key_Point"),
    path('student-life-learning/<str:level>',views.studentLifeLearning,name="Student_life"),

    #subpages news 
    path('news/<str:slug>',views.newsViewPage,name="view_news"),

    #subpages facilities 
    path('facilities/view/<str:slug>',views.facilitiesViewPage,name="view_facility"),
    
    #events subpages 
    path('events/get/',views.getEvents,name="get_events"), 

    #news subpages 
    path('news/get/',views.getNews,name="get_news"),
] 
