from django.urls import path
from . import views
from . import api_views

urlpatterns = [

    # =============================
    # CART TEMPLATE VIEWS
    # =============================

    path("", views.cart_view, name="cart"),

    path(
        "add/<int:product_id>/",
        views.add_to_cart,
        name="add_to_cart"
    ),

    path(
        "update/<int:item_id>/",
        views.update_quantity,
        name="update_quantity"
    ),

    path(
        "remove/<int:item_id>/",
        views.remove_item,
        name="remove_item"
    ),


    # =============================
    # CART API (DRF)
    # =============================

    path("api/cart/", api_views.view_cart, name="api_cart"),

    path("api/cart/add/", api_views.add_to_cart, name="api_add_cart"),

    path("api/cart/update/", api_views.update_cart, name="api_update_cart"),

    path("api/cart/remove/", api_views.remove_item, name="api_remove_cart"),

]