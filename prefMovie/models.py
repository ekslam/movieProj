from django.db import models
from datetime import datetime

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    releaseDate = models.DateField()
    image = models.ImageField(upload_to= 'images/movies/',width_field='picture_width',height_field='picture_height',max_length=255, null=True, blank=True)

class Users(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birthdate = models.DateField()
    