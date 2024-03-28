from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseNotFound
from .forms import CarForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Car

# Create your views here.

@login_required
def index(request):
    return render(request, "employee_portal/index.html")

#def login(request):
    #return render(request, "employee_portal/login.html")

@login_required
def logout_interface(request):
    return render(request, "employee_portal/logout_interface.html")

@login_required
def addCarView(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a new URL: adjust as necessary
    else:
        form = CarForm()
    return render(request, 'employee_portal/addCar.html', {'form': form})

@login_required
def stock_list(request):
    cars = Car.objects.all()  # Fetch all car objects from the database
    return render(request, 'employee_portal/stock_list.html', {'cars': cars})

@require_POST
@csrf_exempt  # Uncomment if you're handling CSRF token manually in the frontend
@login_required
def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    car.delete()
    return JsonResponse({'success': True, 'message': f'Car with ID {car_id} has been deleted.'})

@require_http_methods(["GET"])
@login_required
def find_car(request):
    car_id = request.GET.get('id')
    if not car_id:
        return HttpResponseNotFound("Car ID not provided")

    try:
        car = Car.objects.get(id=car_id)
        # Serialize the car object's details into a dictionary
        data = {
            'id': car.id,
            'brand': car.brand,
            'model': car.model,
            'model_year': car.model_year,
            'kilometres': car.kilometres,
            'color': car.color,
            'engine_capacity': car.engine_capacity,
            'fuel_type': car.fuel_type,
            'doors': car.doors,
            'gearbox_type': car.gearbox_type,
            'price': car.price,
        }
        return JsonResponse(data)
    except Car.DoesNotExist:
        return HttpResponseNotFound("Car not found")
    
@login_required    
def deleteCarView(request):
    return render(request, "employee_portal/deleteCar.html") 
@login_required
def editCarView(request):
    return render(request, "employee_portal/editCar.html") 

@login_required
@require_POST
@csrf_exempt
def update_car(request, car_id):
    # Assuming you have a Car model with an id field
    car = get_object_or_404(Car, id=car_id)
    car.brand = request.POST.get('brand')
    car.model = request.POST.get('model')
    car.model_year = request.POST.get('model_year')
    car.kilometres = request.POST.get('kilometres')
    car.engine_capacity = request.POST.get('engine_capacity')
    car.fuel_type = request.POST.get('fuel_type')
    car.doors = request.POST.get('doors')
    car.gearbox_type = request.POST.get('gearbox_type')
    car.price = request.POST.get('price')
    # Update other fields similarly
    car.save()
    return JsonResponse({'success': True})


    