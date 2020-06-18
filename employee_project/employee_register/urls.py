from django.urls import path, include
from . import views

app_name = "employee_register"

urlpatterns = [
    path('', views.index, name="index"),
    path('personal_info/', views.personal_info, name="personal_info"),
    path('job_info/', views.job_info, name="job_info"),
]