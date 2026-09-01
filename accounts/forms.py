from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=150
    )
    email = forms.EmailField()

    password = forms.CharField(
        widget=forms.PasswordInput
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput
    )
    role = forms.ChoiceField(
        choices=UserProfile.ROLE_CHOICES
    )
    phone = forms.CharField(
        max_length=15
    )
    organization_name = forms.CharField(
        max_length=150,
        required=False
    )
    address = forms.CharField(
        widget=forms.Textarea,
        required=False
    )
    def clean_username(self):
        username = self.cleaned_data['username']

        if User.objects.filter(
            username=username
        ).exists():
            raise forms.ValidationError(
                "Username already exists."
            )

        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get(
            'confirm_password'
        )
        if password and confirm_password:

            if password != confirm_password:

                raise forms.ValidationError(
                    "Passwords do not match."
                )

        return cleaned_data