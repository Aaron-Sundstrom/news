from django.contrib import admin
from .models import CustomUser, AvailableClass

admin.site.register(CustomUser)
admin.site.register(AvailableClass)
