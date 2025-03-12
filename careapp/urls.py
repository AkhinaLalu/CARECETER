from django.urls import path
from .views import StaffRegister,SendOTPView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',StaffRegister.as_view(),name='staff-register'),
    path("send-otp/", SendOTPView.as_view(), name="send_otp"),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
