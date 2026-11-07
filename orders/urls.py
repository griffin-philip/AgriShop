from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('success/<int:order_id>/', views.order_success, name='order_success'),
    path('<int:order_id>/', views.order_detail, name='order_detail'),
    path('farmer-orders/', views.farmer_orders, name='farmer_orders'),
    path("admin/orders/", views.admin_orders, name="admin_orders"),
    path(
        "admin/orders/<int:order_id>/<str:status>/",
        views.update_order_status,
        name="update_order_status"
    ),
]