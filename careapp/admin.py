from django.contrib import admin
from .models import StaffDetails,OTPModel,Certificate

# Register your models here.

admin.site.register(StaffDetails)
admin.site.register(OTPModel)
admin.site.register(Certificate)