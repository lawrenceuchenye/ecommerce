from django.contrib.auth import get_user_model
from apps.order.models import Order,OrderItem
from apps.cart.cart import Cart
from .models import Product

User=get_user_model()

def checkout(request,username,email,address):
  cart=Cart(request)
  order=Order.objects.create(user=User.objects.filter(email=email)[0],email=email,address=address)
  order.save()                                                    
  for item in cart:
    OrderItem.objects.create(order=order,product=Product.objects.get(id=item["product_id"]),quantity=item["quantity"],price=item["price"])
  return order.id


