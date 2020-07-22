from django.contrib import admin
from .models import Facility, Address, Description
# Register your models here.

admin.site.register(Facility)
admin.site.register(Address)
admin.site.register(Description)