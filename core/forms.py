from django import forms
from django.core.validators import RegexValidator
from django.forms import ModelForm
from .models import Client


class SignUpForm(forms.ModelForm):
    client_name = forms.CharField(max_length=30, required=True)
    contact_name = forms.CharField(max_length=30, required=False)
    suburb = forms.CharField(max_length=30, required=False)
    street_name =  forms.CharField(max_length=30, required=False ,widget=forms.TextInput(attrs={'placeholder': '1234 Main St'}))
    postcode = forms.CharField(max_length=10,required=False)
    state = forms.CharField(max_length=10,required=False)
    email = forms.EmailField(max_length=254, required=True,widget=forms.TextInput(attrs={'placeholder': 'abc@gmail.com'}))
    contact_no=forms.CharField(required=True)
   
    class Meta:
        model = Client
        fields = ('client_name', 'contact_name','email','street_name','suburb','postcode','state','contact_no')
        

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and Client.objects.filter(email=email).count() > 0:
            raise forms.ValidationError('This email address is already registered.')
        return email

    def clean_client_name(self):
        client_name = self.cleaned_data.get('client_name')
        if client_name and Client.objects.filter(client_name=client_name).count() > 0:
            raise forms.ValidationError('This client name is already registered.')
        return client_name
    


class UpdateProfile(forms.ModelForm):
        client_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'readonly':'readonly'}))
        contact_name = forms.CharField(max_length=30, required=False)
        suburb = forms.CharField(max_length=30, required=False)
        street_name =  forms.CharField(max_length=30, required=False)
        postcode = forms.CharField(max_length=10,required=False)
        state = forms.CharField(max_length=10,required=False)
        email = forms.EmailField(max_length=254, required=True)
        contact_no=forms.CharField(required=True)
        class Meta:
            model = Client
            fields = ( 'client_name','contact_name','email','street_name','suburb','postcode','state','contact_no')
            
