from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F
from products.models import Product
from orders.models import OrderItem


@login_required
def dashboard(request):
    if request.user.role != "FARMER":
        return redirect('home')

    # Farmer products
    products = Product.objects.filter(farmer=request.user)

    total_products = products.count()

    # Orders related to farmer's products
    order_items = OrderItem.objects.filter(
        product__farmer=request.user,
    )

    total_orders = order_items.count()

    earnings_items = order_items.filter(order__status="DELIVERED")

    total_earnings = earnings_items.aggregate(
        total=Sum(F('price') * F('quantity'))
    )['total'] or 0

    # Low stock products
    low_stock_products = products.filter(stock__lt=5)

    # Recent orders
    recent_orders = order_items.order_by('-order__created_at')[:5]

    context = {
        'total_products': total_products,
        'total_orders': total_orders,
        'total_earnings': total_earnings,
        'low_stock_products': low_stock_products,
        'recent_orders': recent_orders,
    }

    return render(request, 'dashboard/dashboard.html', context)