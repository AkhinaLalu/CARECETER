from django import forms
from .models import StaffDetails
from captcha.fields import CaptchaField


# class StaffDetailsForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#     confirm_password = forms.CharField(widget=forms.PasswordInput())
#     captcha = CaptchaField()

#     class Meta:
#         model = StaffDetails
#         fields = ['first_name', 'last_name', 'email', 'country_code', 'phone_number', 
#                   'password', 'job_applied', 'dob', 'preferred_areas', 'house_number', 
#                   'address', 'nationality', 'gender', 'image', 'captcha']

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")

#         if password and confirm_password and password != confirm_password:
#             self.add_error("confirm_password", "Passwords do not match!")

#         return cleaned_data


class StaffDetailsForm(forms.ModelForm):

    class Meta:
        model = StaffDetails
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password', 'job_applied', 'dob', 
                  'preferred_areas', 'house_number', 'address', 'nationality', 'postal_code','gender', 'image']



# class StaffDetailsForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#     confirm_password = forms.CharField(widget=forms.PasswordInput())
#     captcha = CaptchaField()  
    
#     class Meta:
#         model = StaffDetails
#         fields = ['first_name', 'last_name', 'email', 'country_code', 'phone_number', 
#                   'password', 'job_applied', 'dob', 'preferred_areas', 'house_number', 
#                   'address', 'nationality', 'gender', 'image' ,'captcha']
    
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")

#         if password and confirm_password and password != confirm_password:
#             self.add_error("confirm_password", "Passwords do not match!")

#         return cleaned_data

class EmailForm(forms.Form):
    email = forms.EmailField()

class OTPVerifyForm(forms.Form):
    email = forms.EmailField()
    otp = forms.CharField(max_length=6)