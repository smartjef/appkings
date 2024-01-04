from django import forms
from .models import Contact, BlogComment, Survey, discover_choices, recommend_choices
from phonenumber_field.formfields import PhoneNumberField

class CommentForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name*'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email*'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Comment*', 'style': 'line-height: 1.1em;'})
    )

    class Meta:
        model = BlogComment
        fields = ['name', 'email', 'message']
        exclude = ('blog', 'is_active')

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name*'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email*'})
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject*'})
    )
    phone_number = PhoneNumberField(
        widget=forms.TextInput(attrs={'type':'tel', 'class': 'form-control', 'placeholder': 'Phone number e.g +...'}),
        required=False
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Message*', 'style': 'line-height: 1.1em;'})
    )
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ('is_addressed',)

class SurveyForm(forms.ModelForm):
    name = forms.CharField(
        max_length=120,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
        label='Full Name',
    )
    email = forms.EmailField(
        max_length=120,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
        label='Email',
    )
    phone_number = PhoneNumberField(
        widget=forms.TextInput(attrs={'type':'tel', 'class': 'form-control', 'placeholder': 'Enter your phone number, e.g +...'}),
        label='Phone Number',
    )
    discover_method = forms.ChoiceField(
        choices = discover_choices,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='How did you discover Appkings Solution?',
    )

    liked_about_us = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2, 'class': 'form-control my-2 br-0', 'style': 'line-height: 1.1em;'}),
        label='What did you like About Us?',
    )

    recommend_to_friends = forms.ChoiceField(
        choices = recommend_choices,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Would you recommend Us to your Friends',
    )

    improvements_needed = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2, 'class': 'form-control my-2 br-0', 'style': 'line-height: 1.1em;'}),
        label='What would you like Us to adjust or improve on?',
    )

    additional_suggestions = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2, 'class': 'form-control my-2 br-0', 'style': 'line-height: 1.1em;'}),
        label='Any Other Suggestions for Us?',
    )
    class Meta:
        model = Survey
        fields = '__all__'