from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard_view(request):
   firstname=request.user.username.split()[0]
   orders=len(request.user.user_orders.all())
   wishlist=len(request.user.wishlist.all())
   transactions=len(request.user.user_orders.filter(paid=True))
   return render(request,"dashboard.html",{"firstname":firstname,"wishlist":wishlist,"orders":orders,"transactions":transactions})
          
@login_required
def usersettings_view(request,username):
  print(username)
  return render(request,"usersettings.html",{})
