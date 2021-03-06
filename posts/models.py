from django.db import models
import datetime
from django.urls import reverse
from cloudinary.models import CloudinaryField
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField


class category(models.Model):
    title = models.CharField(max_length =20)
    class Meta:
        verbose_name_plural= '5. CATÉGORIES'
    def __str__(self):
        return self.title



class post(models.Model):
    title = models.CharField(max_length = 150)
    overview =  RichTextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    thumnail = CloudinaryField('image')
    categories = models.ManyToManyField('Category',related_name="packages" , blank = True)
    featured = models.BooleanField()
    date_added = models.DateField('date published',auto_now_add=True)
    video_display = models.BooleanField()
    image_display = models.BooleanField(default = False)
    video = EmbedVideoField(blank = True)
      
       
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
    images = CloudinaryField('image')

 
    def __str__(self):
        return self.post.title

