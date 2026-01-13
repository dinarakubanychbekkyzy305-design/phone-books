# phones/models.py
from django.db import models

class Phone(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    cover = models.ImageField(upload_to='covers/')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
