from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

class Second(models.Model):
    name1=models.CharField(max_length=250)
    img1=models.ImageField(upload_to='pics')
    desc1=models.TextField()

class First(models.Model):
    name0 = models.CharField(max_length=250)
    img0 = models.ImageField(upload_to='pics')
    desc0 = models.TextField()

    def __str__(self):
        return  self.name

    def __str__(self):
        return  self.name1

    def __str__(self):
        return  self.name0