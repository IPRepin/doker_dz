from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=60)
    date = models.DateField()
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='blog/images')
    url = models.URLField(blank=True)

# Create your models here.
