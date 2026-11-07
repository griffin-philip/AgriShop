from products.models import Product
from django.db import models
from django.db import models
from django.conf import settings


class Order(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("CONFIRMED", "Confirmed"),
        ("DELIVERED", "Delivered"),
    ]

    PAYMENT_CHOICES = [
        ("COD", "Cash on Delivery"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES,
        default="COD"
    )

    address = models.TextField()

    phone = models.CharField(max_length=15)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product.name