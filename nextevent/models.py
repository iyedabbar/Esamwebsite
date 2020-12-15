from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class nextevent(models.Model):
    eventname = models.CharField(max_length = 150)
    eventdate = models.CharField(max_length = 150)
    eventtime = models.CharField(max_length = 150)
    eventloction = models.CharField(max_length = 150)
    thumnail = CloudinaryField('image')
    
  

    def __str__(self):
        return self.eventname


# Create your models here.

# Create your models here.
