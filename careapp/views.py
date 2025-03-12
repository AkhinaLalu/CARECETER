import random
import logging
import json
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import StaffDetailsForm,EmailForm
from . models import StaffDetails,OTPModel,Certificate
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.utils.timezone import now

# Create your views here.

# class StaffRegister(View):
#     template_name = "staffregister.html"

#     def get(self, request):
#         """
#         Render the Staff Register page with an empty form.
#         """
#         form = StaffDetailsForm()
#         return render(request, self.template_name, {"form": form})

#     def post(self, request):
#         """
#         Handle form submission.
#         """
#         form = StaffDetailsForm(request.POST, request.FILES)
#         errors = {}


#         if not request.POST.get("job_apply"): 
#             errors["job_apply"] = "Please select a job position."

#         if not request.POST.get("first_name", "").isalpha(): 
#             errors["first_name"] = "Only letters are allowed."
        
#         if not request.POST.get("last_name", "").isalpha(): 
#             errors["last_name"] = "Only letters are allowed."

#         if StaffDetails.objects.filter(email=request.POST.get("email_id")).exists():
#             errors["email_id"] = "Email already registered."

#         if request.POST.get("psw1") != request.POST.get("psw2"):
#             errors["psw1"] = "The password and confirm password must match."
#             errors["psw2"] = "The password and confirm password must match."

#         if not request.POST.get("ph_number", "").isdigit():
#             errors["ph_number"] = "Accept only numbers."

#         if errors:
#             return render(request, self.template_name, {"form": form, "errors": errors})
        


#         StaffDetails.objects.create(
#             # Create and save the object
#         first_name=request.POST.get("first_name"),
#         last_name=request.POST.get("last_name"),
#         email=request.POST.get("email_id"),
#         country_code=request.POST.get("cntry-code"),
#         phone_number=request.POST.get("ph_number"),
#         password=request.POST.get("psw1"),
#         confirm_password=request.POST.get("psw2"),
#         job_applied=request.POST.get("job_apply"),
#         dob=request.POST.get("dob"),
#         preferred_areas=request.POST.get("preferred_areas"),
#         house_number=request.POST.get("house_number"),
#         address=request.POST.get("address"),
#         nationality=request.POST.get("nationality"),
#         gender=request.POST.get("gender"),
#         image=request.FILES.get("image"),
#         certificate=request.FILES.get("certificate"),
#     )

#         if form.is_valid():
#             form.save()
#             messages.success(request, "Application submitted successfully!")
#             return redirect("staff-register")  # Redirect to success page
#         else:
#             messages.error(request, "There was an error in your submission.")
        
#         # Return the form with errors if invalid
#         return render(request, self.template_name, {"form": form})



# class StaffRegister(View):
#     template_name = "staffregister.html"

#     def get(self, request):
#         form = StaffDetailsForm()
#         return render(request, self.template_name, {"form": form})

    # def post(self, request):
    #     form = StaffDetailsForm(request.POST, request.FILES)
    #     errors = {}

    #     if not request.POST.get("job_apply"):
    #         errors["job_apply"] = "Please select a job position."

    #     if not request.POST.get("first_name", "").isalpha():
    #         errors["first_name"] = "Only letters are allowed."

    #     if not request.POST.get("last_name", "").isalpha():
    #         errors["last_name"] = "Only letters are allowed."

    #     if StaffDetails.objects.filter(email=request.POST.get("email_id")).exists():
    #         errors["email_id"] = "Email already registered."

    #     if request.POST.get("psw1") != request.POST.get("psw2"):
    #         errors["psw1"] = "The password and confirm password must match."
    #         errors["psw2"] = "The password and confirm password must match."

    #     if not request.POST.get("ph_number", "").isdigit():
    #         errors["ph_number"] = "Accept only numbers."

    #     if errors:
    #         return render(request, self.template_name, {"form": form, "errors": errors})
        
    #     StaffDetails.objects.create(
    #         # Create and save the object
    #     first_name=request.POST.get("first_name"),
    #     last_name=request.POST.get("last_name"),
    #     email=request.POST.get("email_id"),
    #     country_code=request.POST.get("cntry-code"),
    #     phone_number=request.POST.get("ph_number"),
    #     password=request.POST.get("psw1"),
    #     confirm_password=request.POST.get("psw2"),
    #     job_applied=request.POST.get("job_apply"),
    #     dob=request.POST.get("dob"),
    #     preferred_areas=request.POST.get("preferred_areas"),
    #     house_number=request.POST.get("house_number"),
    #     address=request.POST.get("address"),
    #     nationality=request.POST.get("nationality"),
    #     gender=request.POST.get("gender"),
    #     image=request.FILES.get("image"),
    #     # certificate=request.FILES.get("certificate"),
    # )

    #     if form.is_valid():
    #         staff = form.save(commit=False)
    #         staff.password = request.POST.get("psw1")
    #         staff.confirm_password = request.POST.get("psw2")
    #         staff.save()

    #         # Save multiple certificates
    #         certificate_files = request.FILES.getlist("certificates")
    #         for file in certificate_files:
    #             Certificate.objects.create(staff=staff, certificate=file)

    #         messages.success(request, "Application submitted successfully!")
    #         return redirect("staff-register")
    #     else:
    #         messages.error(request, "There was an error in your submission.")

    #     return render(request, self.template_name, {"form": form})


class StaffRegister(View):
    template_name = "staffregister.html"

    def get(self, request):
        form = StaffDetailsForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = StaffDetailsForm(request.POST, request.FILES)
        errors = {}

        if not request.POST.get("job_apply"):
            errors["job_apply"] = "Please select a job position."

        if not request.POST.get("first_name", "").isalpha():
            errors["first_name"] = "Only letters are allowed."

        if not request.POST.get("last_name", "").isalpha():
            errors["last_name"] = "Only letters are allowed."

        if StaffDetails.objects.filter(email=request.POST.get("email_id")).exists():
            errors["email_id"] = "Email already registered."

        if request.POST.get("psw1") != request.POST.get("psw2"):
            errors["psw1"] = "The password and confirm password must match."
            errors["psw2"] = "The password and confirm password must match."

        if not request.POST.get("ph_number", "").isdigit():
            errors["ph_number"] = "Accept only numbers."

        if errors:
            return render(request, self.template_name, {"form": form, "errors": errors})
        dob=request.POST.get("dob")
        print(dob,"::::::::::::::::::::::")

        # Save the staff details first
        staff = StaffDetails.objects.create(
            # Create and save the object
        first_name=request.POST.get("first_name"),
        last_name=request.POST.get("last_name"),
        email=request.POST.get("email_id"),
        country_code=request.POST.get("cntry-code"),
        phone_number=request.POST.get("ph_number"),
        password=request.POST.get("psw1"),
        confirm_password=request.POST.get("psw2"),
        job_applied=request.POST.get("job_apply"),
        dob=request.POST.get("dob"),
        preferred_areas=request.POST.getlist("preferred_areas"),
        house_number=request.POST.get("house_number"),
        postal_code=request.POST.get("postal_code"),
        address=request.POST.get("address"),
        nationality=request.POST.get("nationality"),
        gender=request.POST.get("gender"),
        image=request.FILES.get("image"),
        # certificate=request.FILES.get("certificate"),
        )

        staff.save()
        # Save multiple certificates
        certificate_files = request.FILES.getlist("certificate[]")  # Match name attribute in HTML
        for file in certificate_files:
            Certificate.objects.create(staff=staff, certificate=file)

        messages.success(request, "Application submitted successfully!")
        return redirect("staff-register")



logger = logging.getLogger(__name__)

class SendOTPView(View):
    template_name = "send_otp.html"

    def get(self, request):
        form = EmailForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
       
        # form = EmailForm(request.POST)
        # if form.is_valid():
        data = json.loads(request.body)

        email = data.get("email")

        # Generate 6-digit OTP
        otp = data.get("otp")
        print(otp,"::::::::::::::::")

        # Save OTP in the database
        otp_instance, created = OTPModel.objects.update_or_create(
            email=email, defaults={"otp": otp, "created_at": now()}
        )
        otp_instance.save()


        try:
            # Send Email
            send_mail(
                subject="Your OTP Code",
                message=f"Your OTP code is {otp}. It is valid for 5 minutes.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,  # Make sure errors are raised
            )
            logger.info(f"OTP {otp} sent to {email}")  # Log OTP sending
            print(f"OTP {otp} sent to {email}")  # Debugging

            return redirect("verify_otp")
        except Exception as e:
            logger.error(f"Error sending OTP email: {e}")
            return render(
                request,
                self.template_name,
                {"error": "Error sending email. Please try again."},
            )

