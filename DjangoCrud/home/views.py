from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def index(request):
    emp = Employees.objects.all()
    return render(request, 'index.html', {'emp': emp})


def ADD(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        emp = Employees(
            name=name, email=email, address=address, phone=phone
        )
        emp.save()
        return redirect('home')
    return render(request, 'index.html')


def Edit(request):
    emp = Employees.objects.all()
    return redirect(request, 'index.html', {'emp': emp})


def Update(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        emp = Employees(
            id=id, name=name, email=email, address=address, phone=phone
        )
        emp.save()
        return redirect('home')
    return render(request, 'index.html')


def Delete(request):
    id = request.GET['id']
    Employees.objects.get(id=id).delete()
    emp = Employees.objects.all()
    return render(request, 'index.html', {'emp': emp})
