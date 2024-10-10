from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'first_name', 
            'last_name', 
            'phone', 
            'email', 
            'address_line_1', 
            'address_line_2', 
            'country', 
            'state', 
            'city', 
            'order_note'
        ]
        
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
            'address_line_1': forms.TextInput(attrs={'placeholder': 'Address Line 1'}),
            'address_line_2': forms.TextInput(attrs={'placeholder': 'Address Line 2'}),
            'country': forms.Select(attrs={'placeholder': 'Country'}),
            'state': forms.Select(attrs={'placeholder': 'State'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'order_note': forms.Textarea(attrs={'placeholder': 'Order Note'}),
        }

