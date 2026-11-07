from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from products.models import Product


@login_required
def cart_view(request):
    if request.user.role != "CUSTOMER":
        return redirect('home')

    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()

    total = sum(item.total_price() for item in items)

    return render(request, 'cart/cart.html', {
        'items': items,
        'total': total
    })


@login_required
def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    quantity = int(request.POST.get("quantity", 1))

    # Get or create cart for user
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Check if item already exists
    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        item.quantity += quantity
    else:
        item.quantity = quantity

    item.save()

    return redirect("cart")


@login_required
def remove_item(request, item_id):

    item = get_object_or_404(CartItem, id=item_id)

    item.delete()

    return redirect("cart")


@login_required
def update_quantity(request, item_id):

    item = get_object_or_404(CartItem, id=item_id)

    quantity = int(request.POST.get("quantity", 1))

    if quantity > 0:
        item.quantity = quantity
        item.save()
    else:
        item.delete()

    return redirect("cart")