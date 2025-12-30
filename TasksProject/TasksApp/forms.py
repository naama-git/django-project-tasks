from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Member, Team, User


class RegisterForm(UserCreationForm):
        
    team = forms.ModelChoiceField(
        queryset=Team.objects.all(),
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'team']


    
