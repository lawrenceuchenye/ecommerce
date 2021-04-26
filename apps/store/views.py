from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Product,Category
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
    related_products=[related_product for related_product in product.category.products.all()[:5]]
    if product in related_products:
      related_products.remove(product)
    is_in_cart=False
    is_wish_listed=False
    is_rated=False
    cart=Cart(request)
    for item in cart:
       if item["product_id"]==product.id:
         is_in_cart=True
    wishlist=None
    if request.user.is_authenticated:
      wishlist=request.user.wishlist.all()
      if request.user.wishlist.filter(product=product):
        is_wish_listed=True
    if request.user.is_authenticated:
      for rated_item in request.user.rated_items.all():
         if rated_item.product==product:
            is_rated=True
            break  
    return render(request,"product-detail.html",{"related_products":related_products,"product":product,"is_in_cart":is_in_cart,"is_wish_listed":is_wish_listed,"is_rated":is_rated})

