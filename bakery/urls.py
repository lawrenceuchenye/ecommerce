"""bakery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
|Class-based views
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

from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap,CategorySitemap,ProductSitemap

from apps.core.views import home_view,account_view,logout_view
from apps.core.api import api_login,api_signup

from apps.store.views import store_view,category_view,detail_view
from apps.store.api import add_to_cart,remove_from_cart,api_checkout,create_checkout_session,wishlist_item,edit_quantity

from apps.cart.views import cart_view
from apps.cart.webhook import webhook

from apps.order.views import checkout_view,validate_order_view,success_view,order_conf_view

sitemaps={"static":StaticViewSitemap,"category":CategorySitemap,"product":ProductSitemap}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml',sitemap,{"sitemaps":sitemaps},name="django.sitemaps.views.sitemap"),

    path('',home_view,name="home"),
    path('api_login/',api_login,name="api_login"),
    path('api_signup/',api_signup,name="api_signup"),
    path('logout/',logout_view,name="logout"),
    path('account/',account_view,name="account"),

    path('store/',store_view,name="store"),
    path('store/<slug:category_slug>/',category_view,name="category"),
    path('store/<int:product_id>/detail',detail_view,name="detail"),

    path('cart/',cart_view,name="cart"),
    path('webhooks/',webhook,name="webhooks"),
    path('add_to_cart/',add_to_cart,name="add_to_cart"),
    path('remove_from_cart/',remove_from_cart,name="remove_from_cart"),
    path('edit_quantity/',edit_quantity,name="edit_quantity"),
	
    path('create_checkout_session/',create_checkout_session,name="create_checkout_session"),
    path('wishlist/',wishlist_item,name="wishlist"),
    path('checkout/',checkout_view,name="checkout"),
    path('validate/<int:order_id>/',validate_order_view,name="validate"),
    path('success/',success_view,name="success"),
    path('order-confirmation/',order_conf_view,name="order_conf"),
                         
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

