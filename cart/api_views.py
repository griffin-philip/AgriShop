from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import CartItemSerializer


@api_view(['GET'])
def view_cart(request):

    cart, created = Cart.objects.get_or_create(user=request.user)

    items = cart.items.all()
    serializer = CartItemSerializer(items, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def add_to_cart(request):

    product_id = request.data.get("product_id")
    quantity = int(request.data.get("quantity", 1))

    cart, created = Cart.objects.get_or_create(user=request.user)

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product_id=product_id
    )

    if not created:
        item.quantity += quantity
    else:
        item.quantity = quantity

    item.save()

    return Response({"message": "Product added to cart"})


@api_view(['PATCH'])
def update_cart(request):

    item_id = request.data.get("item_id")
    quantity = request.data.get("quantity")

    item = CartItem.objects.get(id=item_id)
    item.quantity = quantity
    item.save()

    return Response({"message": "Cart updated"})


@api_view(['DELETE'])
def remove_item(request):

    item_id = request.data.get("item_id")

    item = CartItem.objects.get(id=item_id)
    item.delete()

    return Response({"message": "Item removed"})


@api_view(['GET'])
def cart_total(request):

    cart = Cart.objects.get(user=request.user)

    total = sum(item.total_price() for item in cart.items.all())

    return Response({"total": total})