from django.db import models
import datetime
from django.urls import reverse
from cloudinary.models import CloudinaryField
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField
# Create your models here.
class event(models.Model):
    title = models.CharField(max_length = 150)
    overview =  RichTextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    thumnail = CloudinaryField('image')
    date_added = models.DateField('date published',auto_now_add=True)
    video_display = models.BooleanField()
    image_display = models.BooleanField(default = False)
    video = EmbedVideoField(blank = True)  
   
 


    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('event-detail', kwargs={
            'id': self.id
        })
    
class PostImage(models.Model):
    Event = models.ForeignKey(event, default=None, on_delete=models.CASCADE)
    images = CloudinaryField('image')

    

    def __str__(self):
        return self.post.title