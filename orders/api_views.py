from rest_framework.decorators import api_view
from rest_framework.response import Response
from cart.models import Cart
from .models import Order


@api_view(['POST'])
def checkout(request):

    cart = Cart.objects.get(user=request.user)

    total = sum(item.total_price() for item in cart.items.all())

    order = Order.objects.create(
        user=request.user,
        total_amount=total
    )

    cart.items.all().delete()

    return Response({
        "message": "Order placed",
        "order_id": order.id
    })