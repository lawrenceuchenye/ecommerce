from django.db import models

# Create your models here.

class Category(models.Model):
   title=models.CharField(max_length=255)
   order=models.IntegerField()
    
   def __str__(self):
     return self.title

   class Meta:
     ordering=["-order"]

class Product(models.Model):
   title=models.CharField(max_length=255)
   product_pic=models.ImageField(upload_to="uploads/products")
   price=models.DecimalField(max_digits=100,decimal_places=2)
   desc=models.TextField(blank=True,null=True)
   is_in_store=models.BooleanField(default=True)
   is_featured=models.BooleanField(default=False)
   is_latest=models.BooleanField(default=True)
   is_exculsive=models.BooleanField(default=False)

   created_at=models.DateTimeField(auto_now_add=True)
   
   class Meta:
      ordering=["-created_at"]



