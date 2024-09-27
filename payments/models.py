from django.db import models


class Transaction(models.Model):
    user_id = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
