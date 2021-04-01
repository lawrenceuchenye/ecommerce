from django.shortcuts import render
from .models import Product

# Create your views here.
def store_view(request):
   products=Product.objects.all()
   return render(request,"store.html",{"products":products})

def detail_view(request,product_id):
   product=Product.objects.get(id=product_id)
   return render(request,"detail.html",{"product":product})
