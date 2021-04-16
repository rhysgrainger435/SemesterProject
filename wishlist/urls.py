from django.urls import path
from . import views

app_name  = 'wishlist'

urlpatterns = [
    path('add/<uuid:product_id>/', views.add_wish, name='add_wish'),
    path('', views.wishlist_detail, name='wishlist_detail'),
    path('remove/<uuid:product_id>/', views.wish_remove, name='wish_remove'),
    path('full_remove/<uuid:product_id>/', views.full_remove, name='full_remove'),
]