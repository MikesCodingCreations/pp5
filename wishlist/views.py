from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_wishlist(request):
  wishlist = request.session.get('wishlist', {}) 
  return render(request, 'wishlist.html', context={'wishlist': wishlist})


def add_to_wishlist(request, item_id):

    product = get_object_or_404(Product, pk=item_id)    
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    wishlist = request.session.get('wishlist', {})

    
    request.session['wishlist'] = wishlist
    return redirect(redirect_url)
    

def adjust_wishlist(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    wishlist = request.session.get('wishlist', {})

    if size:
        if quantity > 0:
            wishlist[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} quantity to {wishlist[item_id]["items_by_size"][size]}')
        else:
            del wishlist[item_id]['items_by_size'][size]
            if not wishlist[item_id]['items_by_size']:
                wishlist.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your wishlist')
    else:
        if quantity > 0:
            wishlist[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {wishlist[item_id]}')
        else:
            wishlist.pop(item_id)
            messages.success(request, f'Removed {product.name} from your wishlist')

    request.session['wishlist'] = wishlist
    return redirect(reverse('view_wishlist'))


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