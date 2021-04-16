from django.contrib import admin
from .models import Order,OrderItem

# Register your models here.


def order_name(obj):
   return "%s %s"%(obj.first_name,obj.last_name)

order_name.short_description="Name"

class OrderItemInline(admin.TabularInline):
   model=OrderItem
   raw_id_fields=["product"]
          
class OrderAdmin(admin.ModelAdmin):
  list_display=["id",order_name,"created_at"]
  list_filter=["created_at","status"]
  search_fields=["first_name","place"]
  inlines=[OrderItemInline]
                     
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
