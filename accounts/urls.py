from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',  views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registration/', views.RegisterView.as_view(), name='registration'),
    path('registration_confirmation/', views.RegistrationConfirmation.as_view(), name='registration_confirmation'),


]
