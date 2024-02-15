from django.shortcuts import render, get_object_or_404
from ..models import Service, Client
from django.urls import reverse
#Services
def index(request):
    context = {
        'title': 'Our Solutions',
        'services' : Service.objects.filter(is_active=True)
    }
    return render(request, 'services/index.html', context)

def detail(request, slug):
    category_url = reverse('core:services')
    service = get_object_or_404(Service, is_active=True, slug=slug)
    context = {
        'title': service.title,
        'category': 'Services',
        'category_url': category_url,
        'clients': Client.objects.filter(is_active=True),
        'services' : Service.objects.filter(is_active=True),
        'service': service,
        'hero_url': service.image.cover_image.url if service.image else None
    }
    return render(request, 'services/detail.html', context)   
