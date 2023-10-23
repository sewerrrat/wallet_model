from django.contrib.auth.models import User
from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Wallet(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    currency = models.ForeignKey(to=Currency, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.currency
