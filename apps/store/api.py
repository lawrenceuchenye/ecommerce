from apps.cart.cart import Cart
from apps.order.models import Order
from django.conf import settings
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .models import Product
from .utils import checkout,wishlist,unwishlist
import json
import stripe


User=get_user_model()

def add_to_cart(request):
    cart=Cart(request)
    data=json.loads(request.body)
    product=Product.objects.get(id=data["product_id"])
    product_qty=product.quantity
    cart.add_to_cart(int(data["product_id"]),int(data["qty"]))
    return JsonResponse({"success":True})


def edit_quantity(request):
   cart=Cart(request)
   data=json.loads(request.body)
   product=Product.objects.get(id=data["product_id"])
   product_qty=product.quantity
   quantity=cart.get_item(data["product_id"])
   if(quantity["quantity"]>data["qty"]):
      product.is_in_store=True
      product.quantity+=1
      product.save()
      cart.add_to_cart(int(data["product_id"]),int(data["qty"]))
   else:
      if product.is_in_store:
         if product.quantity>=1:
            product.quantity-=1
            product.save()
            cart.add_to_cart(int(data["product_id"]),int(data["qty"]))
         else:
            product.is_in_store=False
            product.save()
            return JsonResponse({"success":False})
      else:
        return JsonResponse({"success":False})
   return JsonResponse({"success":True})
 
def remove_from_cart(request):
    cart=Cart(request)
    data=json.loads(request.body)
    cart.remove_from_cart(data["product_id"])
    return JsonResponse({"success":True})

def api_checkout(request):
   data=json.loads(request.body)
   order_id=checkout(request,data["username"],data["email"],data["address"])
   return order_id

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
    if (len(items) == 0):
      return JsonResponse({"error": "No items in cart!", "status": False})

    order_id=api_checkout(request)
    try:
      session=stripe.checkout.Session.create(
        payment_method_types=["card"],
        mode="payment",
        line_items=items,
        success_url="http://127.0.0.1:8000/validate/"+str(order_id)+"/",
        cancel_url="http://127.0.0.1:8000/cart/"
       )
    except Exception:
       return JsonResponse({"status":False,"session":{}})
    order=Order.objects.get(id=order_id)
    order.payment_intent=session.id
    order.paid_amount=cart.get_total()
    order.save()

    return JsonResponse({"session":session, "status":True});

def wishlist_item(request):
    data=json.loads(request.body)
    success = False
    if(data["is_authenticated"]):
       success = wishlist(data["product_id"],data["quantity"],request.user)
    return JsonResponse({"success":success})

def unwishlist_item(request):
    data=json.loads(request.body)
    success = False
    if(data["is_authenticated"]):
       success = unwishlist(data["product_id"], data["quantity"], request.user)
    return JsonResponse({"success":success})
