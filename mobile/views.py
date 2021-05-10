from django.shortcuts import render,redirect
from .models import Product,Order,cart
from .forms import CreateProductForm,OrderForm,UserRegistrationForm,LoginForm,cart_form
from django.contrib.auth import authenticate,login,logout
from .decorators import login_required,admin_only
# Create your views here.

def base(request):
    return render(request,"mobile/base.html")

@login_required
def list_mobiles(request):
    mobiles=Product.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"mobile/listmobiles.html",context)

@admin_only
def add_product(request):
    form=CreateProductForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=CreateProductForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("base")
    return render(request,"mobile/createmobile.html",context)


def get_mobile_object(id):
    return Product.objects.get(id=id)

@login_required
def mobile_detail(request,id):
    mobile=get_mobile_object(id)
    context={}
    context["mobile"]=mobile
    return render(request,"mobile/mobiledetail.html",context)

@admin_only
def mobile_delete(request,id):
    mobile=get_mobile_object(id)
    mobile.delete()
    return redirect("base")

@admin_only
def update(request,id):
    mobile=get_mobile_object(id)
    form=CreateProductForm(instance=mobile)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=CreateProductForm(instance=mobile,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("base")
    return render(request,"mobile/mobileupdate.html",context)

@login_required
def order(request,id):
    product=get_mobile_object(id)
    form=OrderForm(initial={'user':request.user,'product':product})
    context={}
    context["form"]=form
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("base") #it should go to userhome not to listmobile
        else:
            context["form"]=form
            return render((request,"mobile/order.html",context))
    return render(request,"mobile/order.html",context)

@login_required
def remove_order(request,id):
    cart_item=cart.objects.get(id=id)
    cart_item.delete()
    return redirect("mycart")

@login_required
def view_my_orders(request):
    orders=Order.objects.filter(user=request.user)
    context={}
    context["orders"]=orders
    return render(request,"mobile/vieworders.html",context)

@login_required
def cancel_order(request,id):
    order=Order.objects.get(id=id)
    order.status='cancelled'
    order.save()
    return redirect("view")

def registration(request):
    form=UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"mobile/login.html")
        else:
            form=UserRegistrationForm(request.POST)
            context["form"]=form
            return redirect("login")
    return render(request,"mobile/registration.html",context)

def login_user(request):
    context={}
    form=LoginForm
    context["form"]=form
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return render(request,"mobile/index.html")

    return render(request,"mobile/login.html",context)

def signout(request):
    logout(request)
    return redirect("login")

@login_required
def add_cart(request,id):
    product= get_mobile_object(id)
    form=cart_form( initial={"user":request.user,"product":product})

    context = {}
    context["form"] = form
    if request.method=="POST":
        form=cart_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listmobile")
        else:
            form=cart_form(request.POST)
            context = {}
            context["form"] = form
            return render(request,"mobile/cart.html",context)
    return render(request, "mobile/cart.html", context)

@login_required
def my_cart(request):
    cart_item=cart.objects.filter(user=request.user)
    context = {}
    context["cart_item"] = cart_item
    return render(request, "mobile/mycart.html", context)

