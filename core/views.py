from django.shortcuts import render
from .models import infastructure, contactinfo
from core import models
# Create your views here.
def home(request):
    context={'home':'active'}

    return render(request,'core/home.html', context)
def service(request):
    context={'service':'active'}

    return render(request,'core/service.html', context)
def skills(request):
    context={'skill':'active'}
    return render(request,'core/skills.html', context)
def contact(request):
     if request.method=='POST':
        Name = request.POST['Name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        infosave = contactinfo(Name=Name,email=email,subject=subject,message=message)

        infosave.save()
     context={'contact':'active'}
     return render(request,'core/contact.html', context)
