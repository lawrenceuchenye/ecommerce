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
   price=models.FloatField()
   desc=models.TextField(blank=True,null=True)
   is_in_store=models.BooleanField(default=True)
   created_at=models.DateTimeField(auto_now_add=True)

   def snippet_android(self):
       return self.title[:9]+"..."
                           
   def snippet_computer(self):
       return self.title[:10]+"..."

   class Meta:
      ordering=["-created_at"]



