from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.files import File
from apps.order.models import Order
from PIL import Image
from io import BytesIO
from .forms import UserEditForm

User=get_user_model()

# Create your views here.
@login_required
def dashboard_view(request):
   firstname=request.user.username.split()[0]
   orders=len(request.user.user_orders.all())
   wishlist=len(request.user.wishlist.all())
   transactions=len(request.user.user_orders.filter(paid=True))
   sum=0
   for transaction in request.user.user_orders.filter(paid=True):
     sum+=transaction.total_amount
   return render(request,"dashboard.html",{"firstname":firstname,"wishlist":wishlist,"orders":orders,"transactions":transactions,"total_amount_spent":sum})
          
@login_required
def usersettings_view(request,username):
  if(username!=request.user.username):
    return redirect("dashboard")

  user=User.objects.get(username=username)
  data={"username":request.user.username,"email":request.user.email,"address":request.user.userprofile.address,"number":request.user.userprofile.phone_number}
  form=UserEditForm(request.POST or None,initial=data)
  if form.is_valid():                         
      form_data=form.cleaned_data
      user.username=form_data["username"]
      user.email=form_data["email"]
      user.save()
      userprofile=user.userprofile
      if request.FILES.keys():
        userprofile.make_profile(request.FILES.get("profile_picture"))
      userprofile.address=form_data["address"]
      userprofile.phone_number=form_data["number"]
      userprofile.save()
      return redirect("dashboard") 
  return render(request,"usersettings.html",{"form":form})



@login_required
def user_order_view(request):
   orders=request.user.user_orders.all()
   firstname=request.user.username.split()[0]
   return render(request,"userorders.html",{"orders":orders,"firstname":firstname})

@login_required
def user_order_detail_view(request,id):
  order=get_object_or_404(Order,id=id)
  firstname=request.user.username.split()[0]
  if(order.user!=request.user):
      return ("orders")
  return render(request,"order-detail.html",{"order":order,"firstname":firstname})

         
@login_required                  
def user_wishlist_view(request):
   wishlist=request.user.wishlist.all()
   firstname=request.user.username.split()[0]
   return render(request,"userwishlist.html",{"wishlist":wishlist,"firstname":firstname})
                                        
