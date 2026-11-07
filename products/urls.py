from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('my-products/', views.my_products, name='my_products'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
]