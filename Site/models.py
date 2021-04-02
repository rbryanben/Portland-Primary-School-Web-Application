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

class NewsClass(models.Model):
    name = models.CharField(max_length=25,primary_key=True,null=False,blank=False)


class NewsTags(models.Model):
    name = models.CharField(max_length=25,primary_key=True,null=False,blank=False)


class NewsItem(models.Model):
    NewsClass = models.ForeignKey(NewsClass,on_delete=models.CASCADE,null=False)
    title= models.CharField(max_length=50,null=False,primary_key=True,blank=False,default="set unique")
    Heading = models.CharField(max_length=50,null=False,blank=False)
    Subtext = models.TextField(null=False,blank=False)
    SubHeadingOne = models.CharField(max_length=50)
    SubHeadingOneText = models.TextField()
    SubHeadingTwo = models.CharField(max_length=50)
    SubHeadingTwoText = models.TextField()
    points = models.TextField(default="not_set")
    date_posted = models.DateTimeField(auto_created=True,null=False)
    pic1 =models.ImageField(upload_to="media/news",default="media/defaults/null_news_image.jpg")
    pic2 = models.ImageField(upload_to="media/news",default="media/defaults/null_news_image.jpg")
    pic3 = models.ImageField(upload_to="media/news",default="media/defaults/null_news_image.jpg")
    pic4 = models.ImageField(upload_to="media/news",default="media/defaults/null_news_image.jpg")
    pic5 = models.ImageField(upload_to="media/news",default="media/defaults/null_news_image.jpg")
    slug = models.CharField(max_length=50,default="dont_set")
    preview = models.CharField(max_length=89,null=False,default="dont_set")
    tag = models.ForeignKey(NewsTags,null=True,on_delete=models.CASCADE)

@receiver(post_save,sender=NewsItem)
def create_news_item_slug(sender,instance,**kwargs):
    if (instance.slug == "dont_set"):
        instance.slug = slugify(instance.title)
        instance.save()
    if (instance.preview == "dont_set"):
        instance.preview = instance.SubHeadingOneText[0:85] + ' ...'
        instance.save()






    
    
 
