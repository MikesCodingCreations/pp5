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
  size = request.POST.get('product_size', None)

  if not request.user.is_authenticated:
      messages.warning(request, 'You need to be logged in to add to wishlist')
      return redirect('login')

  WishItem.objects.create(user=request.user, product=product, size=size)
  messages.success(request, f'Added {product.name} to your wishlist')

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