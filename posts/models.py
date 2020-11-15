from django.db import models
import datetime
from django.urls import reverse

class category(models.Model):
    title = models.CharField(max_length =20)

    def __str__(self):
        return self.title



class post(models.Model):
    title = models.CharField(max_length = 150)
    overview =  models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    commentcount = models.IntegerField(default=0)
    thumnail = models.ImageField()
    categories = models.ManyToManyField('Category',related_name="packages" , blank = True)
    featured = models.BooleanField()
    date_added = models.DateField('date published',auto_now_add=True)
    
    def __str__(self):
        return self.title
    


    class Meta:
        ordering = ['-id']
    
    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={
            'id': self.id
        })

class PostImage(models.Model):
    Post = models.ForeignKey(post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'posts/')

def __str__(self):
        return self.post.title

