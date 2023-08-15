from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.admin import UserAdmin
from .models import *


class CustomUserAdmin(UserAdmin):
    include = ('date_of_birth')
    form = UserChangeForm
    
    list_display = (
        'email', 'uid', 'first_name', 'last_name'
        )

    fieldsets = (
        ('login data', {
            'fields': ('password', 'uid')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'date_of_birth','country','tel')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )
    
    add_fieldsets = (
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Additional information',{
            'fields': ('tel','country','date_of_birth')        
        }),
        ("Authentication", {
            'fields': ('password1', 'password2')
        })
    )


admin.site.register(Shopper, CustomUserAdmin)