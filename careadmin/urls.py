from django.urls import path
from .views import AdminLoginView,DashboardView,RecruitmentView,ProfileDetailsView

urlpatterns = [
    path("admin/", AdminLoginView.as_view(), name="custom_admin_login"),
    path("dashboard/", DashboardView.as_view(), name="dashboard-page"),
    path("recruitment/", RecruitmentView.as_view(), name="recruitment-page"),
    path("deatils/<int:id>/", ProfileDetailsView.as_view(), name="pro-details-page"),

   

]
