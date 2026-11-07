from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Category
from .forms import ProductForm
from reviews.models import Review
from reviews.forms import ReviewForm
from django.db.models import Avg, Count


# List all products
def product_list(request):

    # Annotate ratings for all products
    products = Product.objects.all().annotate(
        avg_rating=Avg("review__rating"),
        review_count=Count("review")
    )

    categories = Category.objects.all()

    # -------- CATEGORY FILTER --------
    selected_categories = request.GET.getlist("category")

    if selected_categories:
        products = products.filter(category__id__in=selected_categories)

    # -------- SORTING --------
    sort = request.GET.get("sort")

    if sort == "price_low":
        products = products.order_by("price")

    elif sort == "price_high":
        products = products.order_by("-price")

    elif sort == "rating":
        products = products.order_by("-avg_rating")

    context = {
        "products": products,
        "categories": categories,
        "selected_categories": selected_categories,
        "sort": sort
    }

    return render(request, "products/product_list.html", context)


# Product detail
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = Review.objects.filter(product=product)
    sort = request.GET.get('sort', 'latest')

    if sort == "rating":
        reviews = reviews.order_by('-rating')
    else:
        reviews = reviews.order_by('-created_at')

    # ⭐ Average rating
    rating_data = reviews.aggregate(
        avg_rating=Avg('rating'),
        review_count=Count('id')
    )

    avg_rating = rating_data['avg_rating'] or 0
    review_count = rating_data['review_count']


    # ⭐ Rating distribution
    rating_counts = reviews.values('rating').annotate(count=Count('rating'))

    rating_dict = {i: 0 for i in range(1, 6)}

    for r in rating_counts:
        rating_dict[r['rating']] = r['count']

    # ⭐ Calculate percentage for progress bars
    rating_percent = {}

    for star, count in rating_dict.items():
        if review_count > 0:
            rating_percent[star] = (count / review_count) * 100
        else:
            rating_percent[star] = 0

    form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,
        'form': form,
        'avg_rating': round(avg_rating, 1),
        'review_count': review_count,
        'sort': sort,
        'rating_counts': rating_dict,
        'rating_percent': rating_percent,
        'stars': [5,4,3,2,1]
    }
    return render(request, 'products/product_detail.html', context)


# view farmers own product
@login_required
def my_products(request):
    products = Product.objects.filter(
        farmer=request.user
    ).annotate(
        avg_rating=Avg('review__rating'),
        review_count=Count('review')
    )
    return render(request, 'products/my_products.html', {'products': products})


# Add product (Farmer only)
@login_required
def add_product(request):
    if request.user.role != "FARMER":
        return redirect('home')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.farmer = request.user
            product.save()
            return redirect('my_products')
    else:
        form = ProductForm()

    return render(request, 'products/add_product.html', {'form': form})


# Delete product (Farmer only)
@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if product.farmer != request.user:
        return redirect('home')

    if request.method == "POST":
        product.delete()
        return redirect('product_list')

    return redirect('product_detail', pk=pk)


# Edit product (Farmer only)
@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    # Only owner farmer can edit
    if product.farmer != request.user:
        return redirect('home')

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/edit_product.html', {'form': form})