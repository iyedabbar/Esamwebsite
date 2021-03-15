from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class member(models.Model):
    name = models.CharField(max_length = 150)
    facebook = models.URLField(max_length=200 , blank = True)
    linkedin = models.URLField(max_length=200 , blank = True)
    email = models.EmailField(max_length=254 , blank = True)
    photo = CloudinaryField('image')
    Position = models.CharField(max_length = 150)
    message_testimonial = models.TextField(blank = True) 
    testimonial = models.BooleanField()
  

    def __str__(self):
        return self.name


