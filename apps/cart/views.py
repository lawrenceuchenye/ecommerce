from django.shortcuts import render
from django.conf import settings
from .cart import Cart

# Create your views here.
def cart_view(request):
   cart=Cart(request)
   sub_total=sum([item["totalcost"] for item in cart])
   total=sub_total+10
   return render(request,"cart.html",{"cart":cart,"sub_total":sub_total,"total":total,"pub_key":settings.STRIPE_API_PUBLISHABLE_KEY})
