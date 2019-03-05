from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    releaseDate = models.DateField()
    image = models.ImageField(upload_to= 'image/movie/',max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('prefMovie.Movies', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

