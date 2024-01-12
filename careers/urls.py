from . import views
from django.urls import path

app_name = 'careers'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.details, name='detail'),
]