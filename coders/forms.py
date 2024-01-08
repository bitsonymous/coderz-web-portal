from django import forms
from .models import Coders

class CoderForm(forms.ModelForm):
    class Meta:
        model = Coders
        fields = ['coder_number', 'first_name', 'last_name', 'lc_id', 'rating']
        labels = {
            'coder_number' : 'Phone Number', 
            'first_name' : 'First Name' ,
            'last_name' : 'Last Name' ,
            'lc_id' : 'Leetcode Username',
            'rating' : 'Rating'
        }
        widgets = {
            'coder_number' : forms.NumberInput(attrs={'class' : 'form-control'}), 
            'first_name' : forms.TextInput(attrs={'class' : 'form-control'}), 
            'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'lc_id' : forms.TextInput(attrs={'class' : 'form-control'}),
            'rating' : forms.NumberInput(attrs={'class' : 'form-control'})
        }