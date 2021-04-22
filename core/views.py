from django.shortcuts import render
from core.models import infastructure, contactinfo
from core import models
# Create your views here.
def home(request):
    inf= infastructure.objects.all()
    return render(request,'core/home.html',{'infa':inf,'home':'active'})
def service(request):
    inf= infastructure.objects.all()
    return render(request,'core/service.html',{'infa':inf,'service':'active'})
def skills(request):
    inf= infastructure.objects.all()

    return render(request,'core/skills.html', {'infa':inf,'skill':'active'})
def contact(request):

     if request.method=='POST':
        Name = request.POST['Name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        infosave = contactinfo(Name=Name,email=email,subject=subject,message=message)

        infosave.save()
     inf= infastructure.objects.all()
     return render(request,'core/contact.html', {'infa':inf,'contact':'active'})
