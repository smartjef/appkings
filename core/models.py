from django.db import models
from django.urls import reverse 
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class PrimaryImage(models.Model):
    front_image = models.ImageField(upload_to="images/front")
    cover_image = models.ImageField(upload_to="images/back")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.front_image.name
    
    class Meta:
        ordering = ('-created_at',)

class Tag(models.Model):
    title = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True)

    def __str__(self):
        return self.title
    
    def get_products_url(self):
        return reverse('core:products_by_tag', kwargs={'tag_slug':self.slug})
    
    def get_blogs_url(self):
        return reverse('core:blogs_by_tag', kwargs={'tag_slug':self.slug})
    
    class Meta:
        ordering = ('-title',)

#Service Models
class Service(models.Model):
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    image = models.ForeignKey(PrimaryImage, null=True, blank=True, on_delete=models.CASCADE ,related_name='services')
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('core:service_detail', kwargs={'slug':self.slug})
    
    class Meta:
        ordering = ('-created_at',)

CLIENT_CATEGORY = (
    ('UNIVERSITIES', 'UNIVERSITIES'),
    ('PARASTATALS', 'PARASTATALS'),
    ('TERTIARY INSTITUTES', 'TERTIARY INSTITUTES'), 
    ('PRIVATE SECTOR INDUSTRIES', 'PRIVATE SECTOR INDUSTRIES'),
    ('NON GOVERNMENT ORGANIZATIONS (NGOs)', 'NON GOVERNMENT ORGANIZATIONS (NGOs)'),
)
class Client(models.Model):
    title = models.CharField(max_length=120, unique=True)
    category = models.CharField(choices=CLIENT_CATEGORY, max_length=50, default='UNIVERSITIES')
    website = models.URLField(max_length=150, unique=True, null=True, blank=True)
    logo = models.ImageField(upload_to='clients/')
    is_active = models.BooleanField(default=True)
    description = models.TextField(help_text='include the features here', max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created_at',)

class Product(models.Model):
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    image = models.ForeignKey(PrimaryImage, null=True, blank=True, on_delete=models.CASCADE, related_name='products')
    is_active = models.BooleanField(default=True)
    clients = models.ManyToManyField(Client, blank=True,  related_name='products')
    services = models.ManyToManyField(Service, blank=True,  related_name='products')
    tags = models.ManyToManyField(Tag, blank=True,  related_name='products')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('core:product_detail', kwargs={'slug':self.slug})
    
    class Meta:
        ordering = ('-created_at',)

class RelatedImage(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, related_name='related_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/images/")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title
    
    class Meta:
        ordering = ('-created_at',)

class Patner(models.Model):
    title = models.CharField(max_length=120, unique=True)
    website = models.URLField(max_length=200, unique=True, null=True, blank=True)
    logo = models.ImageField(upload_to='partners/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created_at',)

class Award(models.Model):
    title = models.CharField(max_length=120, unique=True)
    image = models.ImageField(upload_to='awards/', verbose_name='Certificate')
    summary = models.TextField(null=True, blank=True, max_length=250)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created_at',)

class FAQ(models.Model):
    question = models.CharField(max_length=120, unique=True)
    answer = models.TextField(null=True, blank=True, max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ('-created_at',)


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=200)
    phone_number = PhoneNumberField(null=True, blank=True)
    subject = models.CharField(max_length=120)
    message = models.TextField(max_length=500)
    is_addressed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    
    class Meta:
        ordering = ('-created_at',)
        unique_together = ('name', 'subject')

class Review(models.Model):
    name = models.CharField(max_length=120)
    ratings = models.PositiveSmallIntegerField(choices=((1,1),(2,2),(3,3),(4,4),(5,5)), default=5)
    position = models.CharField(max_length=20)
    image = models.ImageField(upload_to='reviews/', null=True, blank=True)
    message = models.TextField(max_length=300)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-created_at',)
        unique_together = ('name', 'position')

class Blog(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='blogs')
    image = models.ForeignKey(PrimaryImage, null=True, blank=True, on_delete=models.CASCADE, related_name='blogs')
    is_published = models.BooleanField(default=True)
    published_at = models.DateField()
    tags = models.ManyToManyField(Tag, blank=True,  related_name='blogs')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('core:blog_detail', kwargs={'slug':self.slug})
    
    class Meta:
        ordering = ('-created_at',)

class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    message = models.TextField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} commented {self.message}"
    
    class Meta:
        ordering = ('-created_at',)

discover_choices = (
    ("From a Friend", "From a Friend"),
    ("From Social Media", "From Social Media"),
    ("From Our Website", "From Our Website"),
    ("By Myself", "By Myself"),
)

recommend_choices = (
    ("Yes", "Yes"),
    ("No", "No"),
)

class Survey(models.Model):
    name = models.CharField(max_length=120, verbose_name="Name")
    email = models.EmailField(max_length=255)
    phone_number = PhoneNumberField()
    discover_method = models.CharField(
        max_length=50, choices=discover_choices, verbose_name="How did you discover Appkings Solution?"
    )
    liked_about_us = models.TextField(verbose_name="What did you like About Us?")
    recommend_to_friends = models.CharField(
        max_length=3, choices=recommend_choices, verbose_name="Would you recommend Us to your Friends?"
    )
    improvements_needed = models.TextField(verbose_name="What would you like Us to adjust or improve on?")
    additional_suggestions = models.TextField(verbose_name="Any Other Suggestions for Us?")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Survey - {self.name}"
    
    class Meta:
        ordering = ('-created_at',)

class Gallery(models.Model):
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Gallery"
    
    class Meta:
        ordering = ('-created_at',)

class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="gallery/")
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name
    
    class Meta:
        ordering = ('-created_at',)

class Team(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='team')
    image = models.ImageField(upload_to='team/')
    phone_number = PhoneNumberField()
    linkedin = models.URLField(null=True, blank=True)
    position = models.CharField(max_length=120, help_text='e.g Chief Executive Officer')
    order = models.PositiveSmallIntegerField(unique=True, help_text='e.g 1')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    class Meta:
        ordering = ['order']