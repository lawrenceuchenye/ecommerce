from django.conf import settings
from apps.store.models import Product

class Cart(object):
   def __init__(self,request):
     self.sessions=request.session
     cart=self.sessions.get(settings.CART_SESSION_ID)
     if not cart:
       cart=self.sessions[settings.CART_SESSION_ID]={}
     self.cart=cart

   def add_to_cart(self,product_id,quantity):
     product=Product.objects.get(id=product_id)
     item={"product_id":product.id,"quantity":quantity,"price":float(product.price),"totalcost":float(quantity*product.price)}
     self.cart[str(product_id)]=item
     self.save()

   def remove_from_cart(self,product_id):
     del self.cart[str(product_id)]
     self.save()
   
   def items_length(self):
      return sum([item["quantity"] for item in self.cart.values()])
	                                
   def __iter__(self):
       for key in self.cart.keys():
          self.cart[key]["product"]=Product.objects.get(id=int(key))
       for item in self.cart.values():
         yield item
       
   def save(self):
      self.sessions[settings.CART_SESSION_ID]=self.cart
      self.sessions.modified=True
   
   def get_total(self):
      return sum([item["totalcost"] for item in self.cart.values()])
                            
   def clear(self):
      del self.sessions[settings.CART_SESSION_ID]
      self.sessions.modified=True
