from django.shortcuts import render, redirect
from ..models import FAQ, Client, Review, Award
from ..forms import ContactForm, SurveyForm
from django.contrib import messages

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
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            contact.save()
            messages.success(request, 'Form submitted successfully.')
            return redirect('core:index')
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