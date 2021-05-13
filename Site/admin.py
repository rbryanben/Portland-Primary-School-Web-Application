from django.contrib import admin
from . import models #models

#portland
admin.site.register(models.HomePageContent)
admin.site.register(models.KeyPoint)
admin.site.register(models.SchoolLevel)
admin.site.register(models.NewsClass)
admin.site.register(models.NewsItem)
admin.site.register(models.NewsTags)

#facilitites
admin.site.register(models.FacilitiesPageContent)
admin.site.register(models.SchoolFacility)

#academics
admin.site.register(models.AcademicsPageContent)
admin.site.register(models.TopStudent)

#filing system
admin.site.register(models.Folder)
admin.site.register(models.Image)

#events 
admin.site.register(models.Sport)
admin.site.register(models.EventType)
admin.site.register(models.Event)

#admissions
admin.site.register(models.AdmissionsPageContent)


