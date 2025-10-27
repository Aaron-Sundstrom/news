from django.urls import path
from .views import tutor_register

urlpatterns = [
    path("signup/",tutor_register,name="signup"),
]
