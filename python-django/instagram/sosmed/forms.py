from django import forms
from .models import Instagram

class InstagramForm(forms.ModelForm):
    class Meta:
        model = Instagram
        fields = [
            'nama_depan',
            'nama_belakang',
            'username',
            'content',
        ]
        
        widgets = {
            'nama_depan': forms.TextInput(
                attrs={'placeholder':'Masukkan nama depan'}
            ),
            'nama_belakang': forms.TextInput(
                attrs={'placeholder':'Masukkan nama belakang'}
            ),
            'username': forms.TextInput(
                attrs={'placeholder':'Masukkan username'}
            ),
        }