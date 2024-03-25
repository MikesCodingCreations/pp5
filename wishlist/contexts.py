from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from wishlist.models import WishItem

def wishlist_contents(request):

    wishlist_items = []
    total = 0
    product_count = 0
    wishlist = request.session.get('wishlist', {})

    for item_id, item_data in wishlist.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            wishlist_items.append({
                'item_id': item_id,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
    
    context = {
        'wishlist_items': wishlist_items,
    }

    return context