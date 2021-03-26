from django.shortcuts import render

# Create your views here.
def home_view(request):
   return render(request,"home.html",{})

def account_view(request):
  if request.method=="POST":
    print(request.POST)
  return render(request,"account.html",{})
                             
