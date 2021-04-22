from django.db import models

# Create your models here.
class infastructure(models.Model):
    pic = models.ImageField()
    name = models.CharField(max_length=20)
    para1 = models.TextField(max_length=300)
    para2 = models.TextField(max_length=300)
    def __str__(self):
        return self.name

class contactinfo(models.Model):
    Name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=500)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.Name
