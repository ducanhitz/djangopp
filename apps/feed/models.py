import django.contrib.auth.models
from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone
from apps.users.models import User

# Create your models here.
class Post(models.Model):
    description = models.CharField(max_length=255, blank=True)
    pic = models.ImageField(upload_to='feed/')
    date_posted = models.DateTimeField(default=timezone.now)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = CharField(max_length=100, blank=True)

    def __str__(self):
        return self.description
