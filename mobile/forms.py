from django.forms import ModelForm
from .models import Product,Order,cart
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CreateProductForm(ModelForm):
    class Meta:
        model=Product
        fields="__all__"
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'productname'}),
            'price': forms.NumberInput(attrs={'class': 'text_inp', 'placeholder': 'price'}),
            'specs': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'specs'}),

        }


class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields=["address","product","user"]

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","password1","password2","email"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()



class cart_form(ModelForm):
    class Meta:
        model=cart
        fields="__all__"
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'qty': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.TextInput(attrs={'class': 'form-control'}),

        }
