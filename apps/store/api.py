from apps.cart.cart import Cart
from apps.order.models import Order
from django.conf import settings
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .models import Product,Rate
from .utils import checkout,wishlist
import json
import stripe


User=get_user_model()

def add_to_cart(request):
    cart=Cart(request)
    data=json.loads(request.body)
    product=Product.objects.get(id=data["product_id"])
    if product.quantity>data["qty"]:
      product.quantity-=data["qty"]
      product.save()
      cart.add_to_cart(int(data["product_id"]),int(data["qty"]))
    else:
       rm_qty=product.quantity
       product.quantity=0
       product.save()
       cart.add_to_cart(int(data["product_id"]),rm_qty)
       return JsonResponse({"success":False})
    return JsonResponse({"success":True})


def edit_quantity(request):
   cart=Cart(request)
   data=json.loads(request.body)
   product=Product.objects.get(id=data["product_id"])
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
    product=Product.objects.get(id=data["product_id"])
    product.quantity+=data["quantity"]
    product.is_in_store=True
    product.save()
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
       return JsonResponse({"status":False,"error":"Sorry, an error occurred!","session":{}})
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
    wishlist=request.user.wishlist.get(id=data["wishlist_id"])
    wishlist.delete()
    return JsonResponse({"success":True})

def rate(request):
   data=json.loads(request.body)
   if request.user.is_authenticated==False:
    return JsonResponse({"success":False})
   product=Product.objects.get(id=data["product_id"])
   amount=(5/len(User.objects.all()))/5
   if data["event"]=="add":
     product.ratings+=amount
   else:
     product.ratings-=amount
   product.save()
   if request.user.rated_items.filter(product=product).exists()==False:
       Rate.objects.create(user=request.user,product=product)
   return JsonResponse({"success":True})
