from django.shortcuts import render
from .models import Contact
from django.db.models.signals import post_save
from django.template.response import TemplateResponse

# Create your views here.
def contact(request):

    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        subject=request.POST.get('subject')
        contact.message=message
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        success = 'Thank you'
        soon = 'we will contact you soon !'
        return TemplateResponse(request, 'contactcopy.html', { 'success' : success , 'name' : name , 'soon' : soon  })
    else:
        return render (request, "contact.html" )


