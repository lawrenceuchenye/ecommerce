from django.shortcuts import render
from django.conf import settings

# Create your views here.
def checkout_view(request):
   return render(request,"checkout.html",{"pub_key":settings.STRIPE_API_PUBLISHABLE_KEY})
                                                                            
