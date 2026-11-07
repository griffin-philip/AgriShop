from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Review
from .forms import ReviewForm
from django.contrib import messages


@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    existing_review = Review.objects.filter(
        product=product,
        user=request.user
    ).first()

    if existing_review:
        messages.warning(request, "You have already reviewed this product.")
        return redirect("product_detail", pk=product.id)

    rating = request.POST.get("rating")
    comment = request.POST.get("comment")

    Review.objects.create(
        product=product,
        user=request.user,
        rating=rating,
        comment=comment
    )

    messages.success(request, "Review submitted successfully.")
    return redirect("product_detail", pk=product.id)


@login_required
def edit_review(request, review_id):

    review = get_object_or_404(Review, id=review_id)

    if review.user != request.user:
        return redirect('home')

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=review.product.id)

    else:
        form = ReviewForm(instance=review)

    return render(request, 'reviews/edit_review.html', {'form': form})


@login_required
def delete_review(request, review_id):

    review = get_object_or_404(Review, id=review_id)

    if review.user != request.user:
        return redirect('home')

    product_id = review.product.id
    review.delete()

    return redirect('product_detail', pk=product_id)