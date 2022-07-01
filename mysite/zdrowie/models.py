import os
from django.conf import settings
from django.db import models
from django.contrib import admin

def images_path():
    # return os.path.join(settings.BASE_DIR, 'zdrowie/static/zdrowie/images')
    return os.path.join('zdrowie/static/zdrowie/images')
    # return os.path.join(settings.STATIC_URL, 'zdrowie/images')

class Tag(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(default='None')
    # image = models.FilePathField(path=images_path)
    # image = models.FilePathField(path=images_path, recursive=True)
    image = models.FilePathField(path='zdrowie/static/zdrowie/images')
    # image = models.ImageField
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title






