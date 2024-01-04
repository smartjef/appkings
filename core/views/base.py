from django.shortcuts import render, redirect
from ..models import FAQ, Client, Review, Award, GalleryImage, Gallery, Team, Blog, Product, Service
from ..forms import ContactForm, SurveyForm
from django.contrib import messages
from django.http import Http404

def index(request):
    context = {
        'title': 'Homepage',
        'clients': Client.objects.filter(is_active=True),
        'reviews': Review.objects.filter(is_active=True)[:3]
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'title': 'About Us',
        'clients': Client.objects.filter(is_active=True)
    }
    return render(request, 'about.html', context)

def contact(request):
    if request.method == 'POST':
        try:
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Form submitted successfully.')
                return redirect('core:index')
        except Exception as e:
            messages.success(request, f'Error:{e}.')
            return redirect('core:contact')
    else:
        form = ContactForm()

    context = {
        'title': 'Contact Us',
        'reviews': Review.objects.filter(is_active=True),
        'form': form
    }
    return render(request, 'contact.html', context)

def awards(request):
    context = {
        'title': 'Awards & Recognition',
        'faqs': FAQ.objects.filter(is_active=True)[:3],
        'awards': Award.objects.filter(is_active=True),
    }
    return render(request, 'awards.html', context)

def survey(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Feedback Submitted successfully')
            return redirect('core:index')
        else:
            error_messages = form.errors.as_text()
            messages.warning(request, f'Form validation failed: \n{error_messages}')
            return redirect('core:survey')
    else:
        form = SurveyForm()

    context = {
        'title': 'Survey',
        'form': form
    }
    return render(request, 'survey.html', context)

def terms(request):
    context = {
        'title': 'Terms & Condition',
    }
    return render(request, 'terms.html', context)

def privacy(request):
    context = {
        'title': 'Privacy Policy',
    }
    return render(request, 'privacy.html', context)

def faq(request):
    context = {
        'title': 'Frequently Asked Questions',
        'faqs': FAQ.objects.filter(is_active=True),
    }
    return render(request, 'faqs.html', context)

def team(request):
    teams = Team.objects.filter(is_active=True)
    if not teams:
        raise Http404
    
    context = {
        'title': 'Our Team',
        'teams': teams

    }
    return render(request, 'team.html', context)

def gallery(request):
    if not Gallery.objects.filter(is_active=True).first():
        raise Http404

    context = {
        'title': 'Our Gallery',
        'images': GalleryImage.objects.filter(is_active=True)
    }
    return render(request, 'gallery.html', context)

def search(request):
    title = 'Search ...'
    services = blogs = teams = clients = products = awards = faqs = None
    query = request.GET.get('q')

    if query:
        title = f"Results for '{query}'"
        services = Service.objects.filter(title__icontains=query, is_active=True) or Service.objects.filter(description__icontains=query, is_active=True)
        blogs = Blog.objects.filter(title__icontains=query, is_published=True) or Blog.objects.filter(description__icontains=query, is_published=True)
        teams = Team.objects.filter(user__first_name__icontains=query, is_active=True) or Team.objects.filter(user__last_name__icontains=query, is_active=True) or Team.objects.filter(position__icontains=query, is_active=True)
        clients = Client.objects.filter(title__icontains=query, is_active=True)
        products = Product.objects.filter(title__icontains=query, is_active=True) or Product.objects.filter(description__icontains=query, is_active=True)
        awards = Award.objects.filter(title__icontains=query)
        faqs = FAQ.objects.filter(question__icontains=query)

    context = {
        'title': title,
        'services': services,
        'blogs': blogs,
        'teams': teams,
        'clients': clients,
        'products': products,
        'awards': awards,
        'faqs': faqs,
    }

    return render(request, 'search.html', context)