from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home', views.index, name='home'),
    path('login', auth_views.LoginView.as_view(template_name='employee_portal/login.html'), name='login'),
    path('addCar', views.addCarView, name='addCar'),
    path('deleteCar', views.deleteCarView, name='deleteCar'),
    path('editCar', views.editCarView, name='editCar'),
    path('stock_list', views.stock_list, name='stock_list'),
    path('logout', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('logout_interface', views.logout_interface, name='logut_interface'),
    path('find_car/', views.find_car, name='find_car'),
    path('delete_car/<int:car_id>/', views.delete_car, name='delete_car'),
    path('update_car/<int:car_id>/', views.update_car, name='update_car'),
]