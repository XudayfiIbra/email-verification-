from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('email_verification/<slug:username>', views.email_verify, name="email_verification"),
    path('sigin', views.singin, name="sigin")
]
