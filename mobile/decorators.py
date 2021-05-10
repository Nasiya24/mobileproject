from django.shortcuts import redirect

def login_required(func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        return func(request,*args,**kwargs)
    return wrapper

def admin_only(func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_superuser:
            return redirect("login")
        return func(request,*args,**kwargs)
    return wrapper