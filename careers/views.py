from django.shortcuts import render, get_object_or_404
from .models import Job
from django.urls import reverse

# Create your views here.
def index(request):
    context = {
        'title':'Careers',
        'jobs': Job.objects.filter(is_active=True)
    }
    return render(request, 'careers/index.html', context)

def details(request, slug):
    job = get_object_or_404(Job, is_active=True, slug=slug)
    context = {
        'category': 'Careers',
        'category_url' : reverse('careers:index'),
        'title': job.title,
        'job': job
    }
    return render(request, 'careers/details.html', context)