from django.db import models
from slugify import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

class HomePageContent(models.Model):
    HomeBackgroundImage =  models.ImageField(null=False,upload_to="media/home")
    HomeVideoFileYoutubeUrl = models.TextField(null=False)

class KeyPoint(models.Model):
    image1 = models.ImageField(null=False,blank=False, upload_to="media/keypoints")
    image2 = models.ImageField(null=False,blank=False, upload_to="media/keypoints")
    image3 = models.ImageField(null=False, blank=False,upload_to="media/keypoints")
    header = models.CharField(null=False,blank=False,max_length=50)
    subtext = models.TextField(null=False)
    slug  = models.CharField(max_length=50,default="dont_set")
    preview = models.CharField(max_length=89,default="dont_set")


@receiver(post_save, sender=KeyPoint, dispatch_uid="create_slug")
def generate_keypoint_slugs(sender, instance, **kwargs):
    if (instance.slug == "dont_set"):
        instance.slug = slugify(instance.header)
        instance.save()
    if (instance.preview == "dont_set"):
        instance.preview = instance.subtext[0:86] + "..."
        instance.save()


class SchoolLevel(models.Model):
    level = models.CharField(max_length=20,blank=False, null=False,primary_key=True)
    startingGrade = models.IntegerField(default=1,null=False,blank=False)
    endingGrade = models.IntegerField(default=3,null=False,blank=False)
    mainSubText = models.TextField(null=False)
    subTextHeader = models.CharField(max_length=40,null=False)
    subtext = models.TextField(null=False)
    
    
 
