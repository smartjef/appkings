from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import RelatedImage, Review, Blog, BlogComment, Patner, PrimaryImage, Product, Client, Award, FAQ, Contact, Service, Tag, Survey, Gallery, GalleryImage, Team
from django.http import HttpResponse
import csv

def export_selected_to_csv(modeladmin, request, queryset):
    model = queryset.model
    field_names = [field.name for field in model._meta.get_fields()]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="exported_csv_file.csv"'

    writer = csv.writer(response)
    writer.writerow(field_names)

    for contact in queryset:
        writer.writerow([getattr(contact, field) for field in field_names])

    return response

export_selected_to_csv.short_description = "Export selected contacts to CSV"

class RelatedImageInline(admin.TabularInline):
    model = RelatedImage
    extra = 0

class BlogCommentInline(admin.TabularInline):
    model = BlogComment
    extra = 0

class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser', 'date_joined', 'last_login']
    ordering = ['date_joined', 'last_login']
    list_filter = ['is_active', 'is_staff', 'is_superuser', 'date_joined', 'last_login']
    list_per_page = 20

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'created_at', 'updated_at']
    search_fields = ['title', 'slug', 'description']
    list_filter = ['is_active', 'created_at', 'updated_at', 'tags', 'clients', 'services']
    date_hierarchy = 'created_at'
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ['tags', 'clients', 'services', 'image']
    list_per_page = 50
    inlines = [RelatedImageInline]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['message', 'name', 'ratings', 'position', 'is_active', 'created_at']
    search_fields = ['meassage', 'name', 'position']
    list_filter = ['is_active', 'created_at', 'ratings']
    date_hierarchy = 'created_at'
    list_per_page = 50

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'is_published', 'published_at', 'created_at', 'updated_at']
    search_fields = ['title', 'slug', 'description']
    list_filter = ['is_published', 'author', 'tags', 'created_at', 'updated_at', 'published_at']
    autocomplete_fields = ['tags', 'author']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    list_per_page = 50
    inlines = [BlogCommentInline]

@admin.register(Patner)
class PatnerAdmin(admin.ModelAdmin):
    list_display = ['title', 'website', 'logo', 'is_active', 'created_at']
    search_fields = ['title', 'website']
    list_filter = ['is_active', 'created_at']
    date_hierarchy = 'created_at'
    list_per_page = 50

@admin.register(PrimaryImage)
class PrimaryImageAdmin(admin.ModelAdmin):
    list_display = ['front_image', 'cover_image', 'created_at']
    search_fields = ['front_image', 'cover_image']
    list_filter = ['created_at']
    date_hierarchy = 'created_at'
    list_per_page = 50

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'website', 'logo', 'is_active', 'created_at', 'updated_at']
    search_fields = ['title', 'category', 'description', 'website']
    list_filter = ['is_active', 'category', 'created_at', 'updated_at']
    date_hierarchy = 'created_at'
    list_per_page = 50

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'is_active', 'created_at']
    search_fields = ['title', 'summary']
    list_filter = ['is_active', 'created_at']
    date_hierarchy = 'created_at'
    list_per_page = 50

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'is_active', 'created_at']
    search_fields = ['question', 'answer']
    list_filter = ['is_active', 'created_at']
    date_hierarchy = 'created_at'
    list_per_page = 50

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_addressed', 'created_at']
    search_fields = ['name', 'message', 'email', 'subject']
    list_filter = ['is_addressed', 'created_at']
    date_hierarchy = 'created_at'
    list_per_page = 50

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'created_at', 'updated_at']
    search_fields = ['title', 'description', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ['image',]
    list_filter = ['is_active', 'created_at', 'updated_at']
    date_hierarchy = 'created_at'
    list_per_page = 50

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 50

@admin.register(Survey)
class SurvayAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email', 'discover_method', 'recommend_to_friends', 'created_at']
    search_fields = ['name', 'email', 'phone_number', 'discover_method', 'services_offered', 'liked_about_us',]
    list_filter = ['created_at', 'discover_method', 'recommend_to_friends']
    list_per_page = 20
    readonly_fields = ['name', 'email', 'phone_number', 'discover_method', 'liked_about_us', 'recommend_to_friends', 'improvements_needed', 'additional_suggestions', 'created_at']
    actions = [export_selected_to_csv]

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['order', 'user', 'position', 'image', 'is_active', 'created_at', 'updated_at']
    search_fields = ['user__first_name', 'user__last_name', 'position']
    list_filter = ['is_active', 'created_at', 'updated_at']
    list_per_page = 20
    list_display_links = ['user',]

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 0

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at', 'updated_at']
    list_per_page = 20
    inlines = [GalleryImageInline]