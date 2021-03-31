from django.contrib import admin
from . import models #models

#admin site
admin.site.register(models.HomePageContent)
admin.site.register(models.KeyPoint)
admin.site.register(models.SchoolLevel)