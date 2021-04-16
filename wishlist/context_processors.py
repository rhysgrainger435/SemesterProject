from .models import Wishlist, WishlistItem
from .views import _wish_id

def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else: 
        try:
            wishlist = Wishlist.objects.filter(wish_id=_wish_id(request))
            wish_items = WishlistItem.objects.all().filter(wishlist=wishlist[:1])
            for wish_item in wish_items:
                item_count += wish_item.quantity
        except Wishlist.DoesNotExist:
            item_count = 0
    return dict(item_count = item_count)