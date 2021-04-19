from django.shortcuts import render,redirect
from .models import Order
from apps.cart.cart import Cart
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your views here.
def checkout_view(request):
   return render(request,"checkout.html",{"pub_key":settings.STRIPE_API_PUBLISHABLE_KEY})

                  
def validate_order_view(request,order_id):
      cart=Cart(request)
      order=Order.objects.get(id=order_id)
      order.paid=True
      order.save()
      return redirect("order_conf")


def success_view(request):
     return render(request,"success.html",{})

@login_required
def order_conf_view(request):
    cart=Cart(request)
    cart.clear()
    email=request.user.email
    html_string=render_to_string("order-conf-xml.html",{"cart":cart})
    send_mail("Order Confirmation","Please note a service charge of NGN10.00 was added and the exchange rate used was NGN481.00 per $1.00",settings.EMAIL_HOST_USER,[email,settings.EMAIL_HOST_USER],html_message=html_string,fail_silently=False)
                                                                                                                                                                                                                                                
    return render(request,"order-conf.html",{"cart":cart})
