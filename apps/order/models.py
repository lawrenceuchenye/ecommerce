from django.db import models
from apps.store.models import Product
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.
class Order(models.Model):
   ORDERED="ordered"
   SHIPPED="shipped"
   BAKING="baking"

   CHOICES=(
    (ORDERED,"Ordered"),
    (SHIPPED,"Shipped"),
    (BAKING,"Baking"),
   )

   user=models.ForeignKey(User,related_name="user_orders",on_delete=models.CASCADE,null=True)
   email=models.EmailField()          
   address=models.CharField(max_length=255)

   paid=models.BooleanField(default=False)
   total_amount=models.FloatField(blank=True,null=True)
   payment_intent=models.CharField(max_length=255,blank=True)
       
   created_at=models.DateTimeField(auto_now_add=True)
   status=models.CharField(max_length=20,choices=CHOICES,default=ORDERED)
                                         
   def __str__(self):
       return self.email

class OrderItem(models.Model):
    order=models.ForeignKey(Order,related_name="orders",on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name="order_item",on_delete=models.DO_NOTHING)
    quantity=models.IntegerField(default=1)                    
    price=models.FloatField(null=True,blank=True)
                      
    def __str__(self):
       return '%s' % self.id
