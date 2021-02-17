from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def allProdCat(request, category_id=None):
    c_page = None
    products = None
    if category_id != None:
        c_page = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=c_page, available=True)

    else:
        products = Product.objects.all().filter(available=True)

    return render(request, 'phoneshop/category.html', {'category':c_page, 'products':products})

def prod_detail(request, category_id, product_id):
    try:
        product = Product.objects.get(category_id=category_id, id=product_id)
    except Exception as e:
        raise e 
    return render(request, 'phoneshop/product.html', {'product':product})