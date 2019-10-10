from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Client(models.Model):
    client_name = models.CharField(max_length=254,unique=True)
    contact_name = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    street_name = models.CharField(max_length=254)
    suburb = models.CharField(max_length=254)
    postcode_regex = RegexValidator(regex=r'^\+?1?\d{0,10}$', message="invalid postal code")
    postcode = models.CharField(validators=[postcode_regex],max_length=10)
    state = models.CharField(max_length=254)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    contact_no = models.CharField(validators=[phone_regex],max_length=10)

    

    def __str__(self):
        return self.client_name
