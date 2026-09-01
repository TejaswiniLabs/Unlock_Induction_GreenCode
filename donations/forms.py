from django import forms
from .models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = [
            'food_name',
            'food_type',
            'quantity',
            'pickup_location',
            'available_until',
            'description',
            'urgency',
        ]
        widgets = {
            'available_until': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'rows': 4
                }
            ),
            'urgency': forms.NumberInput(
                attrs={
                    'min': 1,
                    'max': 5
                }
            ),
        }