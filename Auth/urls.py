from Auth import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.Register, name="Register"),
    path('', views.Login, name="Login"),
    path('logout', views.Logout, name="Logout"),
    path('dashboard', views.Dashboard, name="Dashboard"),
    path('activateuser/<uidb64>/<token>',views.ActivateAccount, name = 'ActivateAccount'),
]