from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('client-home', views.index, name='client_home'),
    path('allCars', views.allCars, name='allCars'),
    path('carList', views.carBrandsView, name='carList'),
    path('cars-by-brand/<str:brand_name>/', views.cars_by_brand, name='cars_by_brand'),
    #path('login', auth_views.LoginView.as_view(template_name='employee_portal/login.html', next_page='home'), name='login'),
    #path('logout', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    #path('logout_interface', views.logout_interface, name='logout_interface'),
    #path('profile', views.employee_profile, name='profile'),
    #path('editProfile', views.editProfileView, name='editProfile'),

]