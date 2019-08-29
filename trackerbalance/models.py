from django.db import models


# Create your models here.

class Address(models.Model):
    address = models.CharField(max_length=35)
    label = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class BalanceHistory(models.Model):
    balance = models.DecimalField(max_digits=19, decimal_places=2)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='history')
    created_at = models.DateTimeField(auto_now_add=True)

