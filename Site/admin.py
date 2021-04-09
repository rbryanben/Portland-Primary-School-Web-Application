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

