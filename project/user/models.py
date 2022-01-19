from django.db import models


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=True)
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=100, blank=True)


class PostModelUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    created_at = models.CharField(default='1', max_length=100, null=True, blank=True)
    updated_at = models.CharField(max_length=100, null=True, blank=True)
