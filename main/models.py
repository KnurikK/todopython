from django.db import models
from django.utils import timezone


class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class Books(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.TextField(max_length=350)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    genre = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    pub_year = models.DateField(auto_now_add=True)
    reg_date = models.DateTimeField(default=timezone.now)
