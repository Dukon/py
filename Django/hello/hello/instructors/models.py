from django.db import models
from django.conf import settings


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

        
class Position(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
        
class Instructor(models.Model):
    name = models.CharField(verbose_name=u'Instructor Name', max_length=255, help_text="This is name")
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    #phone = models.CharField(max_length=15, null=True, blank=True)
    courses = models.ManyToManyField(Course)
    #course = models.CharField(max_length=255)
    #slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)
    
    position = models.ForeignKey(Position)
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True)
    
    def __str__(self):
        return self.name