from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home', views.index, name='home'),
    path('login', auth_views.LoginView.as_view(template_name='employee_portal/login.html', next_page='home'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('logout_interface', views.logout_interface, name='logout_interface'),
    path('profile', views.employee_profile, name='profile'),
    path('editProfile', views.editProfileView, name='editProfile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('addCar', views.addCarView, name='addCar'),
    path('searchCar', views.searchCarView, name='searchCar'),
    path('deleteCar', views.deleteCarView, name='deleteCar'),
    path('editCar', views.editCarView, name='editCar'),
    path('editCar/<int:car_id>/', views.editCarPageView, name='editCarPage'),
    path('stock_list', views.stock_list, name='stock_list'),
    path('find_car/', views.find_car, name='find_car'),
    path('delete_car/<int:car_id>/', views.delete_car, name='delete_car'),
    path('update_car/<int:car_id>/', views.update_car, name='update_car'),
    #path('client_list', views.client_list, name='client_list'),
    #path('delete-client/<int:client_id>/', views.delete_client, name='delete_client'),

]