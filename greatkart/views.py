from django.shortcuts import render
from store.models import Product, ReviewRating


def home(request):
    products = Product.objects.filter(is_available=True).order_by("created_date")

    for product in products:
        # Get approved reviews for each product
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
        product.reviews = reviews  # attach reviews to each product

        # If your Product model has a method averageReview(), call it here
        product.averageReview = product.averageReview()

    context = {
        "products": products,
    }
    return render(request, "home.html", context)
