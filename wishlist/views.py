from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product
from wishlist.models import WishItem


def view_wishlist(request):
    wish_items = WishItem.objects.filter(user=request.user)
    context = {
        'wish_items': wish_items,
    }

    return render(request, 'wishlist.html', context)

def add_to_wishlist(request, item_id):
    product = get_object_or_404(Product, pk=item_id)    
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    wishlist = request.session.get('wishlist', {})

    if size:
        if item_id in list(wishlist.keys()):
            if size in wishlist[item_id]['items_by_size'].keys():
                wishlist[item_id]['items_by_size'][size] 
                messages.success(request, f'Updated size {size.upper()} quantity to {wishlist[item_id]["items_by_size"][size]}')
            else:
                messages.success(request, f'Added size {size.upper()} {product.name} to your wishlist')
        else:
            wishlist[item_id] = {'items_by_size': {size: size}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your wishlist')
    else:
        if item_id in list(wishlist.keys()):
            wishlist[item_id] 
            messages.success(request, f'Updated {product.name} quantity to {wishlist[item_id]}')
        else:

            messages.success(request, f'Added {product.name} to your wishlist')

    request.session['wishlist'] = wishlist
    return redirect(redirect_url)

def remove_from_wishlist(request, item_id):

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        wishlist = request.session.get('wishlist', {})

        if size:
            del wishlist[item_id]['items_by_size'][size]
            if not wishlist[item_id]['items_by_size']:
                wishlist.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your wishlist')
        else:
            wishlist.pop(item_id)
            messages.success(request, f'Removed {product.name} from your wishlist')

        request.session['wishlist'] = wishlist
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)