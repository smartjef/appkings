from django.contrib import admin
from .models import Job
# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'job_type', 'location', 'is_active', 'created_at', 'updated_at']
    search_fields = ['title', 'slug', 'description']
    list_filter = ['is_active', 'job_type', 'location', 'created_at', 'updated_at']
    date_hierarchy = 'created_at'
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 50
