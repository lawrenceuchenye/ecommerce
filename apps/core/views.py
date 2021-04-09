from django.shortcuts import render,redirect
from .forms import LoginForm,SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login,authenticate,get_user_model
from apps.store.models import Product
     
User=get_user_model()

# Create your views here.
def home_view(request):
   featured=Product.objects.filter(is_featured=True)[:3]
   latest=Product.objects.filter(is_latest=True)[:6]
   exculsive=Product.objects.filter(is_exculsive=True)[0]

   return render(request,"home.html",{"featured":featured,"latest":latest,"exculsive":exculsive})
                                
def login_view(request):
  loginform=LoginForm(request.POST or None)
  if loginform.is_valid():
     user=authenticate(**loginform.cleaned_data)
     login(request,user)
     return redirect("dashboard")
  return render(request,"login.html",{"loginform":loginform})

def signup_view(request):
  signupform=SignupForm(request.POST or None)
  if signupform.is_valid():
      data=signupform.cleaned_data
      del data["conf_password"]
      user=User.objects.create_user(**data)
      user.userprofile
      login(request,user)
      return redirect("home")
  return render(request,"signup.html",{"signupform":signupform})

@login_required
def logout_view(request):
   logout(request)
   return redirect("home")
