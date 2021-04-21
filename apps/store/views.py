from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Product,Category,WishList
from apps.cart.cart import Cart

# Create your views here.
def store_view(request):
   page=request.GET.get("page")
   pages=Paginator(Product.objects.all(),8)
   try:
      page = int(page)
      if (page > pages.num_pages or page < 1):
         page = 1
   except Exception:
      page = 1
   products=pages.page(page)
   exculsive=Product.objects.filter(is_exculsive=True)[0]
   return render(request,"store.html",{"products":products,"exculsive":exculsive})

def category_view(request,category_slug):
   page=request.GET.get("page")
   category=get_object_or_404(Category, slug=category_slug)
   pages=Paginator(category.products.all(),8)
   try:
      page = int(page)
      if (page > pages.num_pages or page < 1):
         page = 1
   except Exception:
      page = 1
   products=pages.page(page)
   return render(request,"category.html",{"products":products,"category":category})

def detail_view(request,product_id):
    product=get_object_or_404(Product, id=product_id)
    related_products=product.category.products.all()[:4]
    is_in_cart=False
    try:
      wishlist=WishList.objects.get(user_id=request.user.id, product_id=product.id)
      is_in_wishlist=bool(wishlist)
      wishlisted_quantity=wishlist.quantity
    except WishList.DoesNotExist:
      wishlist=False
      is_in_wishlist = False
      wishlisted_quantity=1
    print("is_in_wishlist:", is_in_wishlist)
    cart=Cart(request)
    for item in cart:
       if item["product_id"]==product.id:
         is_in_cart=True

    return render(request,"product-detail.html",{"related_products":related_products,"product":product,"is_in_cart":is_in_cart,"is_in_wishlist":is_in_wishlist,"wishlisted_quantity":wishlisted_quantity})
