from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_wishlist(request):
    return render(request, 'wishlist.html')

def add_to_wishlist(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    wishlist = request.session.get('wishlist', {})

    quantity = 1

    if size:
        if not wishlist:  
            wishlist = {} 

        wishlist.setdefault(item_id, {})  
        wishlist[item_id]['items_by_size'].setdefault(size, 0)  
        wishlist[item_id]['items_by_size'][size] += quantity
        messages.success(request, f'Updated size {size.upper()} quantity to {wishlist[item_id]["items_by_size"][size]}')
    else:
        if not wishlist: 
            wishlist = {}  

        wishlist.setdefault(item_id, {})  
        wishlist[item_id].setdefault('quantity', 0)  
        wishlist[item_id]['quantity'] += quantity
        messages.success(request, f'Added {product.name} to your wishlist')

    request.session['wishlist'] = wishlist
    return render(request, 'wishlist.html', context={'wishlist': wishlist})


    if 'wishlist' in request.session:
        return redirect('view_wishlist')
    else:
        messages.warning(request, 'An error occurred. Please try adding the item again.')
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