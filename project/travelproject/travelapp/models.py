from django.db import models
from django.utils.safestring import mark_safe


class Places(models.Model):
    pname = models.CharField(max_length=50)
    pimage = models.ImageField(upload_to='pics')
    pdesc= models.TextField(max_length=100)

