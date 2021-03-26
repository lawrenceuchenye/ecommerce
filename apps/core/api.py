import json
from django.http import JsonResponse
from django.contrib.auth import get_user_model,authenticate
from django.shortcuts import redirect

Users=get_user_model()
    
def verify_user(request):
   data=json.loads(request.body)
   if Users.objects.filter(username=data["username"]).exists():
     if(data["type"]=="login"):
        user=authenticate(request,username=data["username"],password=data["password"])
        if user:
          return JsonResponse({"success":True})
        return JsonResponse({"success":False,"type":"bad-password"})
   else:
      if(data["type"]=="signup"):
         return JsonResponse({"success":True})
      return JsonResponse({"success":False,"type":"bad-username"})

   return JsonResponse({"success":False})
  
