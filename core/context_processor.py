from django.urls import resolve
from .models import Service, Product, Blog, Gallery, Team

def services_products_context(request):
    
    return {
        'services': Service.objects.filter(is_active=True)[:6],
        'products': Product.objects.filter(is_active=True)[:6],
        'blogs': Blog.objects.filter(is_published=True)[:6],
        'gallery': Gallery.objects.filter(is_active=True).first(),
        'team_s': Team.objects.filter(is_active=True).first()
    }

