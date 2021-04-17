from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from apps.store.models import Product

# Create your views here.
def home_view(request):
   featured=Product.objects.filter(is_featured=True)[:3]
   latest=Product.objects.filter(is_latest=True)[:6]
   exculsive=Product.objects.filter(is_exculsive=True)[0]

   return render(request,"home.html",{"featured":featured,"latest":latest,"exculsive":exculsive})

def account_view(request):
   return render(request,"account.html",{})

@login_required
def logout_view(request):
   logout(request)
   return redirect("home")
