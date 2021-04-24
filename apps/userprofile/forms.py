from django import forms
from .models import UserProfile
                         
class UserEditForm(forms.Form):
    username=forms.CharField(label="",max_length=255,widget=forms.TextInput(
    attrs={
    "placeholder":"Username",
    }))                      
    email=forms.EmailField(label="",widget=forms.TextInput(
    attrs={         
    "placeholder":"Email"
    }))     
            
    number=forms.IntegerField(label="",widget=forms.TextInput(
    attrs={
    "placeholder":"Phone Number(Optional)"
    }),required=False)
                      
    address=forms.CharField(label="",max_length=1000,widget=forms.TextInput(
    attrs={
    "placeholder":"Address"                        
    }))     
