
from django.urls import re_path as url
from django.urls import path
from . views import*
from .form import MyChangePasswordForm
from django.contrib.auth.views import LogoutView, PasswordChangeView,PasswordChangeDoneView
urlpatterns = [
    path('',home,name='home'),
    path('contactus/',ContactUs,name="contactus"),
    path('covid19/',Covid19data,name="Covid19"),
    path('aboutus/',AboutUs,name="aboutus"),
    path('chatbot/',Chatbot,name="chatbot"),
    path('signup/',SignupView.as_view(),name="signup"),
    path('login/',MyLoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(next_page="/login/"),name="logout"),
    path('change-password/', PasswordChangeView.as_view( template_name = "core/change-password.html", form_class= MyChangePasswordForm),name="change-password"),
    path('password-change-done/',PasswordChangeDoneView.as_view(template_name="core/password-change-done.html"),name='password_change_done')
]
