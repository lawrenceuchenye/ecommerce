from django.http import JsonResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
                  
import json


User=get_user_model()

def api_login(request):
   data=json.loads(request.body)

   if User.objects.filter(username=data["username"]).exists()==False:
     return JsonResponse({"bad_username":True,"success":False,"bad_password":False})

   user=authenticate(request,password=data["password"],username=data["username"])
   if user==None:
      return JsonResponse({"success":False,"bad_username":False,"bad_password":True})
   login(request,user)

   return JsonResponse({"success":True,"bad_username":False,"bad_password":False})


def api_signup(request):
    data=json.loads(request.body)

    if User.objects.filter(username=data["username"]).exists():
      return JsonResponse({"success":False,"used_username":True})

    if User.objects.filter(email=data["email"]).exists():
      return JsonResponse({"success":False,"used_email":True})

    user=User.objects.create_user(username=data["username"],email=data["email"],password=data["password"])
    userprofile=user.userprofile
    if data["phone_number"]!="":
      userprofile.phone_number=data["phone_number"]
    userprofile.address=data["address"]
    userprofile.save()
  #block 
  #  send_mail("Sign Up Verification","You have successfully signup for an account","lawuche29@gmail.com",["lawuche249@gmail.com","lawuche29@gmail.com"])

    login(request,user)
    return JsonResponse({"success":True,"used_email":False})

