from django.urls import path
from . import views

app_name = 'phoneshop'

urlpatterns = [
    path('', views.allProdCat, name = 'allProdCat'),
    path('<uuid:category_id>/', views.allProdCat, name = 'products_by_category'),
    path('<uuid:cateogry_id>/<uuid:product_id>/', views.prod_detail, name='prod_detail'),
]