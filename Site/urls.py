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
] 
