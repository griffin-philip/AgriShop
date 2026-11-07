from .models import Cart

def cart_item_count(request):
    if request.user.is_authenticated and request.user.role == "CUSTOMER":
        cart, created = Cart.objects.get_or_create(user=request.user)
        count = sum(item.quantity for item in cart.items.all())
        return {'cart_count': count}
    return {'cart_count': 0}