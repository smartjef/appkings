from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from ..models import Blog, Tag
from django.urls import reverse
from ..forms import CommentForm

def index(request, tag_slug=None):
    blogs = Blog.objects.filter(is_published=True)
    tag = None
    query = request.GET.get('q')

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        blogs = blogs.filter(tags=tag)

    if query:
        blogs = blogs.filter(title__icontains=query) | blogs.filter(description__icontains=query)
        title = f"{blogs.count()} records match query '{query}'"
    else:
        title = 'Our Blog'

    context = {
        'title': title,
        'blogs': blogs,
        'tags': Tag.objects.all()
    }
    return render(request, 'blog/index.html', context)

def detail(request, slug):
    blog = get_object_or_404(Blog, is_published=True, slug=slug)
    next_blog = Blog.objects.filter(is_published=True, id__gt=blog.id).order_by('id').first()
    prev_blog = Blog.objects.filter(is_published=True, id__lt=blog.id).order_by('-id').first()
    category_url = reverse('core:blog')
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            messages.success(request, 'Comment submitted successfully.')
            return redirect('core:blog_detail', slug)
    else:
        form = CommentForm()

    context = {
        'title': blog.title,
        'category': 'Blog',
        'category_url': category_url,
        'blog': blog,
#        'hero_url': blog.image.cover_image.url if blog.image else None,
        'tags': Tag.objects.all(),
        'next_blog': next_blog,
        'prev_blog': prev_blog,
        'form': form
    }
    return render(request, 'blog/detail.html', context)
