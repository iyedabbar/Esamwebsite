from django.db import models

# Create your models here.
class Contact (models.Model):
    message = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    
  
    def __str__(self):
        return self.name