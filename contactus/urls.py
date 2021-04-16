from django.contrib import admin
from django.urls import path

from .views import contact_view, successView

app_name = "contactus"

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('success/', successView, name='success'),
]