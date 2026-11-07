from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    farmer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):

    UNIT_CHOICES = [
        ('KG', 'Kilogram (kg)'),
        ('G', 'Gram (g)'),
        ('L', 'Litre (L)'),
        ('ML', 'Millilitre (ml)'),
        ('PCS', 'Pieces'),
        ('BOX', 'Box'),
        ('BAG', 'Bag'),
    ]

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    farmer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default='KG')

    stock = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name