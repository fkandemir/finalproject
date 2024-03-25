from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home', views.index, name='home'),
    path('login', auth_views.LoginView.as_view(template_name='employee_portal/login.html'), name='login'),
    path('addCar', views.addCarView, name='addCar'),
    path('logout', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('logout_interface', views.logout_interface, name='logut_interface'),
]