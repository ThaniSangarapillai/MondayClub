from django.db import models

# Create your models here.

class Stock(models.Model):
    ticker = models.CharField(max_length=5, default="_")
    company_name = models.TextField(default="_")
    price = models.FloatField(default=0)

