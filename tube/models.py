from django.db import models
from django.urls import reverse 
# Create your models here.
class Vod(models.Model):
    title = models.CharField(max_length=50)
    vod = models.FileField( )
    description = models.CharField(max_length=150)
    def get_absolute_url(self):
        return reverse('detail',kwargs={'id':self.id})
