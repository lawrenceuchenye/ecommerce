from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User=get_user_model()
    
dict_pass={}

class LoginForm(forms.Form):
   username=forms.CharField(max_length=255,label="",widget=forms.TextInput(attrs={
     "placeholder":"Username"}))
   password=forms.CharField(max_length=255,label="",widget=forms.PasswordInput(attrs={
     "placeholder":"Password"}))

   def clean_username(self):
      username=self.cleaned_data.get("username")
      if User.objects.filter(username=username).exists():
          return username
      raise forms.ValidationError("*account for "+username+" not found")

   def clean_password(self):
       password=self.cleaned_data.get("password")
       if authenticate(username=self.cleaned_data["username"],password=password):
         return password
       raise forms.ValidationError("*incorrect password")

class SignupForm(forms.Form):
   username=forms.CharField(max_length=255,label="",widget=forms.TextInput(attrs={
     "placeholder":"Username"}))
   email=forms.EmailField(label="",widget=forms.EmailInput(attrs={"placeholder":"Email"}))
   password=forms.CharField(max_length=255,label="",widget=forms.PasswordInput(attrs={
     "placeholder":"Password","id":"password1"}))
   conf_password=forms.CharField(max_length=255,label="",widget=forms.PasswordInput(attrs={
     "placeholder":"Confirm Password","id":"password2"}))


   def clean_username(self):
      username=self.cleaned_data.get("username")
      if User.objects.filter(username=username).exists()==False:
          return username
      raise forms.ValidationError("*username already taken")

   def clean_password(self):
      password=self.cleaned_data.get("password")
      if len(password)<8:
          raise forms.ValidationError("*passwords must be 8 characters")
      dict_pass["password"]=password
      return password
                        
   def clean_conf_password(self):
       password=self.cleaned_data.get("conf_password")
       if password==dict_pass["password"]:
         return password
       raise forms.ValidationError("*passwords must be the same")
