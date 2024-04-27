from django.shortcuts import render
from employee_portal.models import Car
from django.db.models import Count
# Create your views here.

def index(request):
    return render(request, "client_portal/generic_index.html")

def allCars(request):
    cars = Car.objects.all()  # Fetch all car objects from the database
    return render(request, "client_portal/allCars.html", {'cars': cars})
    
def carList(request):
    cars = Car.objects.all()  # Fetch all car objects from the database
    return render(request, "client_portal/carList.html", {'cars': cars})

def cars_by_brand(request, brand_name):
    cars = Car.objects.filter(brand__iexact=brand_name)
    return render(request, 'client_portal/cars_by_brand.html', {'cars': cars, 'brand': brand_name})

def carBrandsView(request):
    brands = Car.objects.values('brand').annotate(count=Count('brand')).order_by('brand')
    return render(request, 'client_portal/carBrands.html', {'brands': brands})

