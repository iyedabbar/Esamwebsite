from django.shortcuts import render
from .models import member
from posts.models import post
# Create your views here.


def index(request):
    Member = member.objects.all()
    testimonial = member.objects.filter(testimonial=True)
    latest_1 = post.objects.order_by('-timestamp')[0:2]
    context = { 'object_list' : Member,
                'object_list_1' : testimonial , 
                'latest_1' : latest_1 ,


    }

    return render(request , 'index.html' , context )