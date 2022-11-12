from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Bike,Car,Other,Reports

class ReportForm(forms.ModelForm):
    class Meta:
        model = Reports
        fields = '__all__'

class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = '__all__'


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class OtherForm(forms.ModelForm):
    class Meta:
        model = Other
        fields = '__all__'



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
