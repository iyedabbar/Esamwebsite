from django.db import models
import datetime
from django.urls import reverse
# Create your models here.
class event(models.Model):
    title = models.CharField(max_length = 150)
    overview =  models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    thumnail = models.FileField(blank=True)
    date_added = models.DateField('date published',auto_now_add=True)
    

    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('event-detail', kwargs={
            'id': self.id
        })
    
class PostImage(models.Model):
    Event = models.ForeignKey(event, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

def __str__(self):
        return self.post.title