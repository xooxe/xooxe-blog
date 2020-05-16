from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png',blank=True)
    #aurthor 
    def __str__(self):
        return self.title