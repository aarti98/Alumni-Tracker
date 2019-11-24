from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
import datetime


# Create your models here.
class Post(models.Model):
    post = models.TextField(null=True)
    date = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


def post_save_receiver(sender, instance, created, **kwargs):
    pass

post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)