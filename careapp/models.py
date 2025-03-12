from django.db import models
from django.utils.timezone import now
from datetime import datetime, timedelta



# Create your models here.

class StaffDetails(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    country_code = models.CharField(max_length=10, default="+1")
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    job_applied = models.CharField(max_length=255, null=True, blank=True)
    dob = models.DateField()
    preferred_areas = models.TextField()
    house_number = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField()
    nationality = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100,default="0000")
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])

    image = models.ImageField(upload_to='applicants/images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Certificate(models.Model):
    staff = models.ForeignKey(StaffDetails, on_delete=models.CASCADE, related_name="certificates")
    certificate = models.FileField(upload_to='applicants/certificates/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Certificate for {self.staff.first_name} {self.staff.last_name}"

class OTPModel(models.Model):
    staff = models.ForeignKey("StaffDetails", null=True, blank=True, on_delete=models.SET_NULL)
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return self.created_at < now() - timedelta(minutes=5)

    def __str__(self):
        return f"{self.email} - {self.otp}"