from django.shortcuts import render, get_object_or_404
from ..models import Product, Tag
from django.urls import reverse

#Products
def index(request, tag_slug=None):
    products = Product.objects.filter(is_active=True)
    if tag_slug:
        products = products.filter(tags=get_object_or_404(Tag, slug=tag_slug))
    context = {
        'title': 'Our Products',
        'products': products
    }
    return render(request, 'products/index.html', context)

def detail(request, slug):
    category_url = reverse('core:products')
    product = get_object_or_404(Product, is_active=True, slug=slug)
    context = {
        'title': product.title,
        'category': 'products',
        'category_url': category_url,
        'product': product,
        'hero_url': product.image.cover_image.url if product.image else None
    }
    return render(request, 'products/detail.html', context)