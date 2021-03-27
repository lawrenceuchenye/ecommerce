import json
from django.http import JsonResponse
from django.contrib.auth import get_user_model,authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

User=get_user_model()

def verify_user(request):
   data=json.loads(request.body)
   if User.objects.filter(username=data["username"]).exists():
     if(data["type"]=="login"):
        user=authenticate(request,username=data["username"],password=data["password"])
        if user:
          login(request,user)
          return JsonResponse({"success":True})
        return JsonResponse({"success":False,"type":"bad-password"})
   else:
      if(data["type"]=="signup"):
         user=User.objects.create(username=data["username"],email=data["email"],password=data["password"])
         user.userprofile
         login(request,user)
         return JsonResponse({"success":True})
      return JsonResponse({"success":False,"type":"bad-username"})

   return JsonResponse({"success":False})

@login_required
def logout_user(request):
   logout(request)
   return redirect("home");
