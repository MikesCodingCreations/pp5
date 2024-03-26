from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product
from wishlist.models import WishItem


def view_wishlist(request):
  wish_items = WishItem.objects.filter(user=request.user)
  context = {
      'wish_items': wish_items,
      'has_wishlist_items': wish_items.exists(),  # Check if any items exist
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
    wish_item = WishItem.objects.get(user=request.user, product__pk=item_id)

    wish_item.delete()
    messages.success(request, f'Removed {wish_item.product.name} from your wishlist')
    return redirect('view_wishlist')

  except WishItem.DoesNotExist:
    messages.warning(request, 'Item not found in your wishlist')
    return redirect('view_wishlist')

  except Exception as e:
    messages.error(request, f'Error removing item: {e}')
    return HttpResponse(status=500)
