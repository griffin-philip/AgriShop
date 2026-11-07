from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),

    # Core pages
    path('', include('core.urls')),

    # Authentication
    path('accounts/', include('accounts.urls')),

    # Products
    path('products/', include('products.urls')),

    # Cart system
    path('cart/', include('cart.urls')),

    # Orders
    path('orders/', include('orders.urls')),

    # Farmer dashboard
    path('dashboard/', include('dashboard.urls')),

    # Reviews
    path('reviews/', include('reviews.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)