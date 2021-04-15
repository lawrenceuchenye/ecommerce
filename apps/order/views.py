from django.shortcuts import render,redirect
from .models import Order
from apps.cart.cart import Cart

from django.conf import settings

# Create your views here.
def checkout_view(request):
   return render(request,"checkout.html",{"pub_key":settings.STRIPE_API_PUBLISHABLE_KEY})

                  
def validate_order_view(request,order_id):
      cart=Cart(request)
      cart.clear()
      order=Order.objects.get(id=order_id)
      order.paid=True
      order.save()
      return redirect("success")


def success_view(request):
     return render(request,"success.html",{})

