from django.shortcuts import render
from employee_portal.models import Car
from django.db.models import Count
from django.http import JsonResponse
import random
from django.db.models import Q  # Import Q for complex queries
# Create your views here.



def index(request):
    # Fetch the latest three cars based on their IDs
    latest_cars = Car.objects.order_by('-id')[:3]
    return render(request, "client_portal/generic_index.html", {'latest_cars': latest_cars})


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

def searchCarView(request):
    query = request.GET.get('query', '')
    if query:
        cars = Car.objects.filter(
            Q(brand__icontains=query) |
            Q(model__icontains=query) |
            Q(price__icontains=query) |
            Q(model_year__icontains=query)
        )
    else:
        cars = Car.objects.none()

    return render(request, 'client_portal/search.html', {'cars': cars, 'request': request})

#def contactView(request):
#    return render(request, "client_portal/client_contact.html")

def aboutusView(request):
    return render(request, "client_portal/aboutUs.html")

