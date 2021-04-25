from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.

class Category(models.Model):
   title=models.CharField(max_length=255)
   slug=models.SlugField(max_length=255)
   order=models.IntegerField()

   def __str__(self):
     return self.title

   def get_absolute_url(self):
     return "/store/%s/"%(self.slug)
             
   class Meta:
     ordering=["-order"]

class Product(models.Model):
   title=models.CharField(max_length=255)
   slug=models.SlugField(max_length=255,null=True,blank=True)
   product_pic=models.ImageField(upload_to="uploads/products")
   price=models.DecimalField(max_digits=100,decimal_places=2)
   desc=models.TextField(blank=True,null=True)

   is_in_store=models.BooleanField(default=True)
   is_featured=models.BooleanField(default=False)
   is_latest=models.BooleanField(default=True)
   is_exculsive=models.BooleanField(default=False)

   quantity=models.IntegerField(default=1)

   created_at=models.DateTimeField(auto_now_add=True)
   category=models.ForeignKey(Category,related_name="products",on_delete=models.CASCADE)


   class Meta:
      ordering=["-created_at"]

   def __str__(self):
      return self.title

   def get_absolute_url(self):
      return "/store/%s/detail"%(self.id)
              
class WishList(models.Model):
     user=models.ForeignKey(User,related_name="wishlist",on_delete=models.CASCADE)
     product=models.ForeignKey(Product,related_name="wishlisted_items",on_delete=models.CASCADE)
     quantity=models.IntegerField(default=1)

     def __str__(self):
       return self.product.title
