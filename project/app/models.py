from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField((""), max_length=254)
    subject = models.CharField(max_length=200)
    body = models.TextField()