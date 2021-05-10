"""mobileproject URL Configuration

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
from django.shortcuts import render
from .views import base,list_mobiles,add_product,mobile_detail,mobile_delete,update,order,view_my_orders,cancel_order,\
    registration,login_user,signout,add_cart,my_cart,remove_order

urlpatterns = [
    path("",base,name="base"),
    path("mobile",list_mobiles,name="listmobile"),
    path("add",add_product,name="addproduct"),
    path("detail/<int:id>",mobile_detail,name="detail"),
    path("delete/<int:id>",mobile_delete,name="delete"),
    path("update/<int:id>",update,name="update"),
    path("order/<int:id>",order,name="order"),
    path("view",view_my_orders,name="view"),
    path("cancel/<int:id>",cancel_order,name="cancel"),
    path("register",registration,name="register"),
    path("login",login_user,name="login"),
    path("logout",signout,name="signout"),
    path("addcart/<int:id>",add_cart,name="addcart"),
    path("mycart",my_cart,name="mycart"),
    path("removeorder",remove_order,name="removeorder")

]
