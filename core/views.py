from django.shortcuts import render
from products.models import Product

def home(request):
    return render(request, 'core/home.html')


def home(request):
    featured_products = Product.objects.all()[:6]

    return render(request, "core/home.html", {
        "featured_products": featured_products
    })