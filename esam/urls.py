from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from posts.views import  blog , post , blog_detail
from Events.views import events, evento_detail
from contacts.views import contact
from team.views import index 
from django.views.generic import TemplateView
 
urlpatterns = [ path('admin/', admin.site.urls),
                path( '', index),
                path('index/', index),
                path('blog/', blog),
                path('blog_detail/<id>/', blog_detail , name ='blog-detail'),
                path('contact/', contact),
                path('events/', events , name ='event-list'),
                path('evento_detail/<id>/', evento_detail , name ='event-detail'),
                path('zohoverify/verifyforzoho.html', TemplateView.as_view(template_name='verifyforzoho.html'))
               
                ]
                





if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)