from django.db import models
from django.contrib.auth.models import User
from apps.order.models import Order

# Create your models here.
class UserProfile(models.Model):
   user=models.OneToOneField(User,on_delete=models.CASCADE)
   phone_number=models.IntegerField(null=True,blank=True)
   address=models.CharField(max_length=255,null=True,blank=True)

                                                

User.userprofile=property(lambda u:UserProfile.objects.get_or_create(user=u)[0])
                                                                 
