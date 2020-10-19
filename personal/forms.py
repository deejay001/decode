from django import forms
from .models import Comment, Customer


class CForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']


class CusForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'message']
