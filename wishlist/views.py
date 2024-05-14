from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product
from wishlist.models import WishItem


def view_wishlist(request):
  wish_items = WishItem.objects.filter(user=request.user)
  context = {
      'wish_items': wish_items,
      'has_wishlist_items': wish_items.exists(), 
  }

  return render(request, 'wishlist.html', context)


def add_to_wishlist(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    size = request.POST.get('product_size', None)

    if not request.user.is_authenticated:
        messages.warning(request, 'You need to be logged in to add to wishlist')
        return redirect('login')

    existing_item = WishItem.objects.filter(user=request.user, product=product, size=size).first()

    if existing_item:
        existing_item.quantity += 1 
        existing_item.save()
        messages.success(request, f'{product.name} quantity updated in your wishlist')
    else:
        WishItem.objects.create(user=request.user, product=product, size=size)
        messages.success(request, f'Added {product.name} to your wishlist')

    return redirect(reverse('view_wishlist'))


def remove_from_wishlist(request, item_id):
    try:
        wish_items = WishItem.objects.filter(user=request.user, product__pk=item_id)

        if not wish_items.exists():
            messages.warning(request, 'Item not found in your wishlist')
            return redirect('view_wishlist')

        wish_item_to_delete = wish_items.first()
        wish_item_to_delete.delete()

        messages.success(request, f'Removed {wish_item_to_delete.product.name} from your wishlist')
        return redirect('view_wishlist')

    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
        return redirect('view_wishlist')