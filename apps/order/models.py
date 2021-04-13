from django.db import models
from apps.store.models import Product

# Create your models here.
class Order(models.Model):
   first_name=models.CharField(max_length=60)
   last_name=models.CharField(max_length=60)
   email=models.EmailField()
   zip_code=models.CharField(max_length=255)
   place=models.CharField(max_length=255)
   address=models.CharField(max_length=255)
  
   paid=models.BooleanField(default=False)
   paid_amount=models.FloatField(blank=True,null=True)
   payment_intent=models.CharField(max_length=255,blank=True)

   created_at=models.DateTimeField(auto_now_add=True)
   
   def __str__(self):
       return self.first_name

class OrderItem(models.Model):
    order=models.ForeignKey(Order,related_name="orders",on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name="order_item",on_delete=models.DO_NOTHING)
    quantity=models.IntegerField(default=1)                    
    price=models.FloatField(null=True,blank=True)
                      
    def __str__(self):
       return '%s' % self.id
