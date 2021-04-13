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
from apps.store.views import store_view,category_view,detail_view
from apps.store.api import add_to_cart,remove_from_cart,api_checkout,create_checkout_session
from apps.cart.views import cart_view
from apps.cart.webhook import webhook
from apps.order.views import checkout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name="home"),
    path('login/',login_view,name="login"),
    path('signup/',signup_view,name="signup"),
    path('logout/',logout_view,name="logout"),

    path('dashboard/',dashboard_view,name="dashboard"),
     
    path('store/',store_view,name="store"),
    path('store/<slug:category_slug>/',category_view,name="category"),
    path('store/<int:product_id>/detail',detail_view,name="detail"),

    path('cart/',cart_view,name="cart"),
    path('webhooks/',webhook,name="webhooks"),
                 
    path('add_to_cart/',add_to_cart,name="add_to_cart"),
    path('remove_from_cart/',remove_from_cart,name="remove_from_cart"),
    path('api_checkout/',api_checkout,name="api_checkout"),
    path('create_checkout_session/',create_checkout_session,name="create_checkout_session"),

    path('checkout/',checkout_view,name="checkout"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
                              
