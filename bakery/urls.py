"""bakery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static 

from apps.core.views import home_view,login_view,signup_view,logout_view
from apps.userprofile.views import dashboard_view
from apps.store.views import store_view,detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name="home"),
    path('login/',login_view,name="account"),
    path('signup/',signup_view,name="signup"),
    path('logout/',logout_view,name="logout"),

    path('dashboard/',dashboard_view,name="dashboard"),
    path('store/',store_view,name="store"),
    path('store/detail/<int:product_id>/',detail_view,name="detail")
                        
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
                              
