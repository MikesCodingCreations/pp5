from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class WishItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=10, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1) 

    def __str__(self):
        return f"{self.quantity} of {self.product}"
