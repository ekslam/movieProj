from django.db import models
from datetime import datetime

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    releaseDate = models.DateField()
    image = models.ImageField(upload_to= 'image/movie/',max_length=255, null=True, blank=True)
