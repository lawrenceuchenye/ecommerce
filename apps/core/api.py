from django.http import JsonResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth import get_user_model

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

    if User.objects.filter(email=data["email"]).exists():
      return JsonResponse({"success":False,"used_email":True})

    user=User.objects.create_user(username=data["username"],email=data["email"],password=data["password"])
    userprofile=user.userprofile
    userprofile.phone_number=data["phone_number"]
    userprofile.address=data["address"]
    userprofile.save()

    login(request,user)
    return JsonResponse({"success":True,"used_email":False})

