from django.shortcuts import render, redirect
from .forms import CarForm

# Create your views here.

def index(request):
    return render(request, "employee_portal/index.html")

def login(request):
    return render(request, "employee_portal/login.html")

def addCarView(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a new URL: adjust as necessary
    else:
        form = CarForm()
    return render(request, 'employee_portal/addCar.html', {'form': form})
    #return render(request, "employee_portal/addCar.html")
