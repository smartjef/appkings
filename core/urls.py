from core.views import services, base, products, blog
from . import views
from django.urls import path

app_name = 'core'
urlpatterns = [
    path('', base.index, name='index'),
    path('about/', base.about, name='about'),
    path('awards/', base.awards, name='awards'),
    path('contact/', base.contact, name='contact'),
    path('survey/', base.survey, name='survey'),
    path('services/', services.index, name='services'),
    path('services/<slug:slug>/', services.detail, name='service_detail'),
    path('products/', products.index, name='products'),
    path('products/tags/<slug:tag_slug>/', products.index, name='products_by_tag'),
    path('products/<slug:slug>/', products.detail, name='product_detail'),
    path('teams/', base.team, name='team'),
    path('gallery/', base.gallery, name='gallery'),
    path('search/', base.search, name='search'),
    path('faqs/', base.faq, name='faqs'),
    path('terms/', base.terms, name='terms'),
    path('privacy/', base.privacy, name='privacy'),
    path('blog/', blog.index, name='blog'),
    path('blog/tags/<slug:tag_slug>/', blog.index, name='blogs_by_tag'),
    path('blog/<slug:slug>/', blog.detail, name='blog_detail'),
]
