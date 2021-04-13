from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product,Category
from apps.cart.cart import Cart

# Create your views here.
def store_view(request):
   page=request.GET.get("page")
   pages=Paginator(Product.objects.all(),8)
   products=pages.page(int(page))
   exculsive=Product.objects.filter(is_exculsive=True)[0]
   return render(request,"store.html",{"products":products,"exculsive":exculsive})

def category_view(request,category_slug):
   page=request.GET.get("page")
   category=Category.objects.get(slug=category_slug)
   pages=Paginator(category.products.all(),8)
   products=pages.page(int(page))
   return render(request,"category.html",{"products":products,"category":category})
                                                  

def detail_view(request,product_id):
    product=Product.objects.get(id=product_id)
    related_products=product.category.products.all()[:4]
    is_in_cart=False
    cart=Cart(request)
    for item in cart:
       if item["product_id"]==product.id:
         is_in_cart=True

    return render(request,"product-detail.html",{"related_products":related_products,"product":product,"is_in_cart":is_in_cart})
