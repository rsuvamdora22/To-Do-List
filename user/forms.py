from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField

class Register(UserCreationForm):
    email = forms.EmailField()
    captcha = ReCaptchaField()
    class Meta:
        model = User
        fields = ['username','email']  
         