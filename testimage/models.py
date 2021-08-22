from django.db import models

# Create your models here.
class Imageupload(models.Model):
    caption = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='image/', default="")