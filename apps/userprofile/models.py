from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
   user=models.OneToOneField(User,on_delete=models.CASCADE)
   profile_pic=models.ImageField(upload_to="uploads/profiles/",blank=True,null=True)

User.userprofile=property(lambda u:UserProfile.objects.get_or_create(user=u)[0])
                                                                 
