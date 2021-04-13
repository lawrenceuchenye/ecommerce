from .cart import Cart

def cart_items(request):
   cart=Cart(request)
   return {"cart_items":cart.items_length()}
          
