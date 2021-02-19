from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    author = models.ManyToManyField(User, blank=True, related_name='blogs')
    title = models.CharField(max_length=256)
    content = models.TextField()
    views = models.IntegerField()
