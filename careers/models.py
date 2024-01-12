from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import striptags, escape
from django.urls import reverse 

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220)
    job_type = models.CharField(choices=(('intership','internship'),('full-time','full-time'), ('part-time','part-time')), max_length=20)
    location = models.CharField(choices=(('on-site','on-site'),('remote','remote'), ('hybrid','hybrid')), max_length=10)
    description = RichTextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('careers:detail', kwargs={'slug':self.slug})
    
    def get_overview(self):
        cleaned_description = striptags(self.description)[:200]
        cleaned_description = escape(cleaned_description)
        return cleaned_description

    
    class Meta:
        ordering = ('-created_at',)