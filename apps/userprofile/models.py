from django.db import models
from django.contrib.auth.models import User
from django.core.files import File
from apps.order.models import Order
from PIL import Image
from io import BytesIO

# Create your models here.
class UserProfile(models.Model):
   user_profile=models.ImageField(upload_to="uploads/profile_pictures",null=True,blank=True)
   user=models.OneToOneField(User,on_delete=models.CASCADE)
   phone_number=models.IntegerField(null=True,blank=True)
   address=models.CharField(max_length=255,null=True,blank=True)

   
   def make_profile(self,image,size=(300,300)):
      img=Image.open(image)
      img.convert("RGB")
      img.thumbnail(size)
      thumb_io=BytesIO()
      img.save(thumb_io,"JPEG",quality=85)
      self.user_profile=File(thumb_io,name=image.name)

User.userprofile=property(lambda u:UserProfile.objects.get_or_create(user=u)[0])

