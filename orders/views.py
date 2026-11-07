from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from .models import Order, OrderItem
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages


@staff_member_required
def admin_orders(request):

    orders = Order.objects.select_related("user").all().order_by("-created_at")

    return render(request, "orders/admin_orders.html", {
        "orders": orders
    })

@login_required
def checkout(request):

    # Only customers allowed
    if request.user.role != "CUSTOMER":
        return redirect('home')

    cart = Cart.objects.get(user=request.user)
    items = cart.items.all()

    # Prevent empty checkout
    if not items:
        return redirect('cart')

    total = sum(item.total_price() for item in items)

    if request.method == "POST":

        address = request.POST.get("address")
        phone = request.POST.get("phone")

        # Create Order
        order = Order.objects.create(
            user=request.user,
            total_amount=total,
            status='CONFIRMED',
            address=address,
            phone=phone,
            payment_method="COD"
        )

        # Create Order Items
        for item in items:
            # Check stock before creating order item
            if item.quantity > item.product.stock:
                messages.error(request, f"{item.product.name} does not have enough stock."
                )
                return redirect("cart")

            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

            # Reduce Stock
            item.product.stock -= item.quantity
            item.product.save()

        # Clear Cart
        items.delete()

        return redirect('order_success', order_id=order.id)

    return render(request, 'orders/checkout.html', {
        'items': items,
        'total': total
    })


@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_success.html', {'order': order})


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/my_orders.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    # Customer can view own order
    if request.user == order.user:
        return render(request, 'orders/order_detail.html', {'order': order})

    return redirect('home')


@login_required
def farmer_orders(request):
    if request.user.role != "FARMER":
        return redirect('home')

    orders = OrderItem.objects.filter(
        product__farmer=request.user
    ).select_related('order', 'product')

    return render(request, 'orders/farmer_orders.html', {'orders': orders})


@staff_member_required
def update_order_status(request, order_id, status):

    order = Order.objects.get(id=order_id)

    order.status = status
    order.save()

    return redirect("admin_orders")