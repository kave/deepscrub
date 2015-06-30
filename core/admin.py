from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from . import models

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms


class PriceAdmin(admin.ModelAdmin):
    pass


class ColorAdmin(admin.ModelAdmin):
    pass


class SpongeTypeAdmin(admin.ModelAdmin):
    pass


class SpongeAdmin(admin.ModelAdmin):
    pass


class ContactUsAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Color, PriceAdmin)
admin.site.register(models.Price, ColorAdmin)
admin.site.register(models.SpongeType, SpongeTypeAdmin)
admin.site.register(models.Sponge, SpongeAdmin)
admin.site.register(models.ContactUs, ContactUsAdmin)
