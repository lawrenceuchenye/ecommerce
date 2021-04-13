from apps.cart.cart import Cart
from apps.order.models import Order
from django.conf import settings
from django.shortcuts import redirect
from django.http import JsonResponse
from .utils import checkout
import json
import stripe
     
def add_to_cart(request):
    cart=Cart(request)
    data=json.loads(request.body)
    cart.add_to_cart(int(data["product_id"]),int(data["qty"]))
    return JsonResponse({"success":True})

      
def remove_from_cart(request):
    cart=Cart(request)
    data=json.loads(request.body)
    cart.remove_from_cart(data["product_id"])
    return JsonResponse({"success":True})

def api_checkout(request,session_intent):
   data=json.loads(request.body)
   order_id=checkout(request,data["firstname"],data["lastname"],data["email"],data["zipcode"],data["place"],data["address"],session_intent)
   order=Order.objects.get(id=order_id)
   paid=True
   cart=Cart(request)
   if paid:
      order.paid=True   
      order.paid_amount=(cart.get_total()+10)
      cart.clear()
   order.save()

def create_checkout_session(request):
    cart=Cart(request)
    stripe.api_key=settings.STRIPE_API_HIDDEN_KEY
    items=[]

    for item in cart:
       product=item["product"]
       obj={
        "price_data":{
           "currency":"usd",
           "product_data":{
            "name":product.title
           },
           "unit_amount":int((product.price/481)*100),
          },                               
           "quantity":item["quantity"]                  
        }

       items.append(obj)

    session=stripe.checkout.Session.create(
     payment_method_types=["card"],
     mode="payment",
     line_items=items,
     success_url="http://127.0.0.1:8000/",
     cancel_url="http://127.0.0.1:8000/cart/"
     )   
    api_checkout(request,session.payment_intent)
    return JsonResponse({"session":session})
                                 
