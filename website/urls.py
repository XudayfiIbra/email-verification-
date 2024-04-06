from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name="signup"),
    path('', views.email_verify, name="email_v"),
]
