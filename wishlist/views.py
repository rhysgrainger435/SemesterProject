from django.shortcuts import render, redirect, get_object_or_404
from phoneshop.models import Product
from .models import Wishlist, WishlistItem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def _wish_id(request):
    wishlist = request.session.session_key
    if not wishlist:
        wishlist = request.session.create()
    return wishlist

def add_wish(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        wishlist = Wishlist.objects.get(wish_id=_wish_id(request))
    except Wishlist.DoesNotExist:
        wishlist = Wishlist.objects.create(
            wish_id=_wish_id(request)
            )
        wishlist.save()
    try:
        wish_item = WishlistItem.objects.get(product=product, wishlist=wishlist)
        wish_item.quantity += 1
        wish_item.save()
    except WishlistItem.DoesNotExist:
        wish_item = WishlistItem.objects.create(
                    product = product,
                    quantity = 1,
                    wishlist = wishlist,
            )
        wish_item.save()
    return redirect('wishlist:wishlist_detail')


def wishlist_detail(request, total=0, counter=0, cart_items = None):
    try:
        wishlist = Wishlist.objects.get(wish_id=_wish_id(request))
        wish_items = WishlistItem.objects.filter(wishlist=wishlist, active=True)
        for wish_item in wish_items:
            total += (wish_item.product.price * wish_item.quantity)
            counter += wish_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'wishlist.html', {'wish_items': wish_items, 'total':total, 'counter':counter})

def wish_remove(request, product_id):
    wishlist = Wishlist.objects.get(wish_id=_wish_id(request))
    product = get_object_or_404(Product, id=product_id)
    wish_item = WishlistItem.objects.get(product=product, wishlist=wishlist)
    if wish_item.quantity > 1:
        wish_item.quantity -= 1
        wish_item.save()
    else:
        wish_item.delete()
    return redirect('wishlist:wishlist_detail')

def full_remove(request, product_id):
    wishlist = Wishlist.objects.get(wish_id=_wish_id(request))
    product = get_object_or_404(Product, id=product_id)
    wish_item = WishlistItem.objects.get(product=product, wishlist=wishlist)
    wish_item.delete()
    return redirect('wishlist:wishlist_detail')
        