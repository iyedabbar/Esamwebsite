from django.shortcuts import render , get_object_or_404
from .models import post , PostImage
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage



def blog(request):
    featured = post.objects.filter(featured=True).order_by('-id')
    latest = post.objects.order_by('-timestamp')[0:6]
    paginator = Paginator(featured, 3)
    page = request.GET.get('page')
    featured = paginator.get_page(page)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    context = {'object_list' : featured,
                'latest': latest,
                'posts': posts,
                'featured ' : featured ,
      
    }
    return render (request, 'blog.html' , context)

def blog_detail(request, id):
    Post = get_object_or_404(post , id=id)
    photos = PostImage.objects.filter(Post=Post)
    context = {
        'Post' : Post ,
        'photos' : photos

    }
    
    return render(request , 'blog_detailscopy.html' , context )




