from django.db import models


# Create your models here.

class Product(models.Model):
    class Meta:
        db_table = "product"

    name = models.CharField(max_length=256, blank=True)
    weight = models.IntegerField(null=True, blank=False)
    price = models.IntegerField(null=True, blank=False)
    created_at = models.CharField(default='1', max_length=100, null=True, blank=True)
    updated_at = models.CharField(max_length=100, null=True, blank=True)
