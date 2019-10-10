from django.contrib import admin
from core.models import Client


@admin.register(Client)
class UserAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'contact_name','email','street_name','suburb','postcode','state','contact_no')
