from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from apps.store.models import Category,Product
                           
              
class StaticViewSitemap(Sitemap):
     def items(self):
        return ["home"]

     def location(self,item):
         return reverse(item)

class CategorySitemap(Sitemap):
     def items(self):
        return Category.objects.all()
 
class ProductSitemap(Sitemap):
     def items(self):
        return Product.objects.all()
