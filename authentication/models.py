from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

PROFILE_CHOICES = [('student', 'Student'),
                    ('alumni', 'Alumni')]


class CustomUser(AbstractUser):
    profile = models.CharField(max_length=10,choices=PROFILE_CHOICES, default='student')


    def __str__(self):
        return self.username


class StudentDetail(models.Model):
    first_name    = models.CharField(max_length=20)
    last_name     = models.CharField(max_length=20) 
    contact_no    = models.IntegerField()
    birth_date    = models.DateField()
    course        = models.CharField(max_length=50)
    session_start = models.IntegerField()
    session_end   = models.IntegerField()
    picture       = models.ImageField(upload_to='images/', null=True, blank=True)
    user          = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.first_name + self.last_name

def post_save_receiver(sender, instance, created, **kwargs):
    pass

post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)


class AlumniDetail(models.Model):
    first_name    = models.CharField(max_length=20)
    last_name     = models.CharField(max_length=20) 
    contact_no    = models.IntegerField()
    birth_date    = models.DateField()
    course        = models.CharField(max_length=50)
    session_start = models.IntegerField()
    session_end   = models.IntegerField()
    company       = models.CharField(max_length=60)
    job_profile   = models.CharField(max_length=20)
    city          = models.CharField(max_length=20)
    skills        = models.TextField(max_length=100)
    about_me      = models.TextField(max_length=100)
    user          = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + self.last_name


def post_save_receiver(sender, instance, created, **kwargs):
    pass

post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)
