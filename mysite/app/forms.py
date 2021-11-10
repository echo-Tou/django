from django import forms
from django.forms import fields

class Auth(forms.Form):
    username = fields.CharField(max_length=10, required=True)   # required 是否是必填
    password = fields.CharField(widget=forms.PasswordInput)    # widget=forms.PasswordInput 密码加密不明文显示
