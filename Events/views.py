from django.shortcuts import render , get_object_or_404
from .models import event , PostImage
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage




def events(request):
    evento = event.objects.all().order_by('-id')
    paginator = Paginator(evento, 8)
    page = request.GET.get('page')
    evento = paginator.get_page(page)
    try:
        posto = paginator.page(page)
    except PageNotAnInteger:
        posto = paginator.page(1)
    except EmptyPage:
        posto = paginator.page(paginator.num_pages)


    context = {'envent_list' : evento,
                'posto': posto,
                'evento ' : evento ,
      
    }
    return render (request, 'program.html' , context)


def evento_detail(request, id):
    Event = get_object_or_404(event , id=id)
    photos = PostImage.objects.filter(Event=Event)
    context = {
        'Event' : Event ,
        'photos' : photos

    }
    
    return render(request , 'blog_details.html' , context )
