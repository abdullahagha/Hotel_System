from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import hotel




class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phoneNum = forms.CharField(max_length=30, required=False, help_text='Optional.')
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email','phoneNum', 'password1', 'password2', )

class HotelForm(forms.ModelForm):

    class Meta:
        model = hotel
        fields = ('Name', 'City', 'Star', 'Location', 'PhoneNum')
'''
class SelectionForm(forms.Forms):
    hotelChoices = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'class': 'recipes-user-products'}),
                                             choices=OPTIONS, label='')'''
