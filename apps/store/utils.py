from apps.order.models import Order,OrderItem
from apps.cart.cart import Cart
from .models import Product
               
def checkout(request,first_name,last_name,email,zip_code,place,address,payment_intent):
  cart=Cart(request)
  order=Order.objects.create(first_name=first_name,last_name=last_name,email=email,zip_code=zip_code,place=place,address=address,payment_intent=payment_intent)
  order.save()
  for item in cart:
    OrderItem.objects.create(order=order,product=Product.objects.get(id=item["product_id"]),quantity=item["quantity"],price=item["price"])
  return order.id

                                          
